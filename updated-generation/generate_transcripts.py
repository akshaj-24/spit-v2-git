from session import Session
import used_patient_IDS
import pandas as pd
from patient import Patient
import questionBank
from prompt import Prompt
import ollama
import requests
import json
import functions
from pydantic import BaseModel, ConfigDict, Field
import output_parser as op
import time
import re

ASCII_PRINTABLE = r"^[\t\n -~]*$"   # tabs/newlines + ASCII 0x20..0x7E

class TextResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str = Field(..., pattern=ASCII_PRINTABLE)

prompt: Prompt = None
session: Session = None

#----------------------------------------------------------------#


# Get random patient not used in previous sessions, set up patient class and set to session
# Does not return anything, modifies session object
def assign_patient():
    
    used_patients = used_patient_IDS.get_patient_IDS()
    df = pd.read_csv("../cactus-non-cm-processed.csv")
    row = df.sample()
    patient_ID = int(row["patient_ID"].values[0])
    while patient_ID in used_patients:
        row = df.sample()
        patient_ID = int(row["patient_ID"].values[0])
    used_patient_IDS.append_ID(patient_ID, session.session_id)
    
    session.patient = Patient()
    session.patient.row = row
    session.patient.update_patient_data()
    prompt.patient = session.patient
 
# Create phase and session transcript file and set to session and state
# Create interviewer and set to prompt
# Does not return anything, modifies session and prompt objects   
def initialize_session():
    pd.DataFrame(columns=["role", "content"]).to_json(f"session_data/{session.session_id}_phase_transcript.jsonl", orient="records", lines=True)
    session.state.phase_transcript = f"session_data/{session.session_id}_phase_transcript.jsonl"
    pd.DataFrame(columns=["role", "content"]).to_json(f"session_data/{session.session_id}_session_transcript.jsonl", orient="records", lines=True)
    session.session_transcript = f"session_data/{session.session_id}_session_transcript.jsonl"
    
    row = pd.DataFrame([{"role": "system", "content": f"--- Session {session.session_id} Start ---\n\n --Patient ID {session.patient.patient_ID}--"}])
    
    row.to_json(session.session_transcript, orient="records", lines=True)
    row.to_json(session.state.phase_transcript, orient="records", lines=True)
    
    prompt.create_interviewer()
    prompt.state = session.state
    
    
# Get phase data from question bank    
def load_phase(phase: int):
    phase_dict = {
        1: questionBank.phase1,
        2: questionBank.phase2,
        3: questionBank.phase3,
        4: questionBank.phase4,
        5: questionBank.phase5,
        6: questionBank.phase6,
        # 7: questionBank.phase7,
    }
    return phase_dict.get(phase, None)

# Update state at end of phase
# Saves phase transcript to session transcript, Updates summaries and patient notes, Resets phase transcript, Advances to next phase
# Does not return anything, modifies session object
def updateState():

    # Save transcript to session transcript
    df = pd.read_json(session.session_transcript, lines=True)
    df = pd.concat([df, pd.read_json(session.state.phase_transcript, lines=True)], ignore_index=True)
    df.loc[len(df)] = ["system", f"--- Phase {session.state.get_current_phase()} End ---"]
    df.to_json(session.session_transcript, orient="records", lines=True)
    
    # Update summaries, patient notes
    dialogue = session.state.get_phase_transcript()
    
    session.state.update_summary(createPhaseSummary(dialogue))
    session.state.update_patient_summary(createPhasePatientSummary(dialogue))
    session.state.update_patient_notes(createPhasePatientNotes(dialogue))
    
    # Reset phase transcript
    session.state.reset_phase_transcript()
    
    session.state.next_phase()
    return 
    
#----------------------------------------------------------------#
#--------------------------    LLM     --------------------------#
#----------------------------------------------------------------#

BASE_URL = "http://localhost:11434"
PATIENT_MODEL = "qwen3:32b"
INTERVIEWER_MODEL = "qwen3:32b"
BASE_MODEL = "qwen3:32b"
PATIENT_OPTIONS = {
    "temperature": 0.9,
    "stop": ["}"],
    "num_ctx": 13288,
}
INTERVIEWER_OPTIONS = {
    "temperature": 0.6,
    "stop": ["}"],
    "num_ctx": 13288,
}
BASE_OPTIONS = {
    "temperature": 0.3,
    "stop": ["}"],
    "num_ctx": 13288,
}
# top_p = 0.9
# top_k = 40

ascii_schema = {
  "type": "object",
  "properties": {
    "text": {
      "type": "string",
      "pattern": r"^[\t\n -~]*$"
    }
  },
  "required": ["text"],
  "additionalProperties": False
}

schema = TextResponse.model_json_schema()

interviewer_model = ollama.Client(host='http://localhost:11434')
patient_model = ollama.Client(host='http://localhost:11434')
base_model = ollama.Client(host='http://localhost:11434')

def get_tokens(resp):
    prompt_match = re.search(r"prompt_eval_count=(\d+)", str(resp))
    # Regex pattern to capture the number after 'eval_count='
    eval_match = re.search(r"eval_count=(\d+)", str(resp))
    prompt_count = int(prompt_match.group(1)) if prompt_match else 0
    eval_count = int(eval_match.group(1)) if eval_match else 0
    total_tokens = prompt_count + eval_count
    print(total_tokens)
    
def get_response_thinking(client, model, prompt_text: str, options, role) -> str:
    
    system = None
    
    if (role == "interviewer"):
        system = """You are a medical psychiatrist interviewer that follows the instructions given by the user. Respond in English with valid JSON with this exact shape:
{
  \"text\": string
}
Do not include any other keys or commentary."""
    elif (role == "patient"):
        system = """You are a medical psychiatrist patient that follows the instructions given by the user. Respond in English with valid JSON with this exact shape:
{
  \"text\": string
}
Do not include any other keys or commentary."""
    elif (role == "system"):
        system = """You are a medical psychiatrist system agent that follows the instructions given by the user. Respond in English with valid JSON with this exact shape:
{
  \"text\": string
}
Do not include any other keys or commentary."""
    
    
    resp = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt_text}
        ],
        #format=schema,
        stream=False,
        options=options,
    )
    return resp

def get_response(client, model, prompt_text: str, options, role, schema) -> str:
    
    system = None
    
    if (role == "interviewer"):
        system = "You are a medical psychiatrist interviewer that follows the instructions given by the user. Return ONLY text matching the schema."
    elif (role == "patient"):
        system = "You are a medical psychiatrist patient that follows the instructions given by the user. Return ONLY JSON matching the schema."
    elif (role == "system"):
        system = "You are a helpful assistant that follows the instructions given by the user. Return ONLY JSON matching the schema."
    
    
    resp = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt_text}
        ],
        format=schema,
        stream=False,
        options=options,
    )
    return resp

def get_interviewer_response(prompt_text: str) -> str:

    resp = get_response_thinking(
        interviewer_model,
        INTERVIEWER_MODEL,
        prompt_text,
        INTERVIEWER_OPTIONS,
        "interviewer",
    )
    
    get_tokens(resp)
    raw = resp["message"]["content"] + "}"
    
    try:
        data = op.extract_first_json(raw)
        content = data["text"]
    except Exception as e:
        print("Recursive call\n\n")
        print(f"Raw {raw} \n\n")
        print(f"Error {e} \n\n")
        print("---------------------------------------------------------------------------------------------------------------------------\n\n")
        return get_interviewer_response(prompt_text)    
    
    print(f"INTERVIEWER: {content}\n")
    return content

def get_patient_response(prompt_text: str) -> str:

    resp = get_response_thinking(
        patient_model,
        PATIENT_MODEL,
        prompt_text,
        PATIENT_OPTIONS,
        "patient",
    )

    get_tokens(resp)
    raw = resp["message"]["content"] + "}"
    
    try:
        data = op.extract_first_json(raw)
        content = data["text"]
    except Exception as e:
        print("Recursive call\n\n")
        print(f"Raw {raw} \n\n")
        print(f"Error {e} \n\n")
        print("---------------------------------------------------------------------------------------------------------------------------\n\n")
        return get_patient_response(prompt_text)   
    
    print(f"PATIENT: {content}\n")
    return content

def get_base_response(prompt_text: str) -> str:
    
    resp = get_response_thinking(
        base_model,
        BASE_MODEL,
        prompt_text,
        BASE_OPTIONS,
        "system",
    )
    
    get_tokens(resp)
    raw = resp["message"]["content"] + "}"
    
    try:
        data = op.extract_first_json(raw)
        content = data["text"]
    except Exception as e:
        print("Recursive call\n\n")
        print(f"Raw {raw} \n\n")
        print(f"Error {e} \n\n")
        print("---------------------------------------------------------------------------------------------------------------------------\n\n")
        return get_base_response(prompt_text)   
    
    
    print(f"SYS: {content}\n")
    return content

def get_summary_response(prompt_text: str) -> str:
    
    resp = get_response_thinking(
        base_model,
        BASE_MODEL,
        prompt_text,
        BASE_OPTIONS,
        "system",
    )

    get_tokens(resp)
    raw = resp["message"]["content"] + "}"
    
    raw = op.extract_first_json(raw)
    
    try:
        subjective = raw["subjective"]
        objective = raw["objective"]
        assessment = raw["assessment"]
        plan = raw["plan"]
        
        content = f"Subjective: {subjective}\n\nObjective: {objective}\n\nAssessment: {assessment}\n\nPlan: {plan}"
        
    except Exception as e:
        print("Recursive call\n\n")
        print(f"Raw {raw} \n\n")
        print(f"Error {e} \n\n")
        print("---------------------------------------------------------------------------------------------------------------------------\n\n")
        return get_summary_response(prompt_text)   
    
    
    print(f"SYS: {content}\n")
    return content

#----------------------------------------------------------------#

def createPhaseSummary(dialogue: str) -> str:
    new = prompt.update_summary_prompt(dialogue)
    summary = get_base_response(new)
    return summary

def createPhasePatientSummary(dialogue: str) -> str:
    new = prompt.update_patient_summary_prompt(dialogue)
    summary = get_base_response(new)
    return summary

def createPhasePatientNotes(dialogue: str) -> str:
    new = prompt.update_patient_notes_prompt(dialogue)
    summary = get_base_response(new)
    return summary


# Create session summary and save to session transcript
def createSessionSummary():
    
    df = pd.read_json(session.session_transcript, lines=True)

    dialogue = "\n".join([f"{row['role']}: {row['content']}" for _, row in df.iterrows()])

    summary = get_summary_response(prompt.session_summary_prompt(dialogue))
    
    df.loc[len(df)] = ["system", f"--- Session Summary ---\n\n{summary}\n\n--- End Summary ---"]
    df.to_json(session.session_transcript, orient="records", lines=True)
    
    return

#-----------------------------------------------------------------#
#-------------------------  MAIN FUNCTION  -----------------------#
#-----------------------------------------------------------------#

def conversation():
    
    global prompt
    global session
    
    prompt = Prompt()
    session = Session()
    
    assign_patient()
    initialize_session()
    
    while True:
        
        # print(session.state.get_current_phase())
        # time.sleep(4)
        
        interviewer_prompt = prompt.create_interviewer_prompt(load_phase(session.state.get_current_phase()))
        interviewer_response = get_interviewer_response(interviewer_prompt)
        
        if interviewer_response == "--FUNCTION-- end_phase --FUNCTION--":
            if functions.end_phase(session) == 1:
                break
            else:
                updateState()
                continue
            
        session.state.add_to_phase_transcript("interviewer", interviewer_response)
        
        patient_prompt = prompt.create_patient_prompt(interviewer_response)
        # print("calling patient response")
        patient_response = get_patient_response(patient_prompt)
        
        session.state.add_to_phase_transcript("patient", patient_response)
        
    createSessionSummary()
    
    return


i = 1
 
 
while True:
    try:
        print(f"------------------------------------------------------ Conversation {i} ---------------------------------------------------------\n")
        conversation()
        print(f"------------------------------------------------------ End {i} ---------------------------------------------------------\n")
        i += 1
    except Exception:
        continue
    
    
print("All Conversations Ended.")
        
#-----------------------------------------------------------------#