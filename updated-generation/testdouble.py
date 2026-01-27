import ollama
import requests
import json

BASE_URL = "http://localhost:11434"
PATIENT_MODEL = "qwen3:32b"
INTERVIEWER_MODEL = "qwen3:32b"
PATIENT_OPTIONS = {
    "temperature": 0.9,
}
INTERVIEWER_OPTIONS = {
    "temperature": 0.6,
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

interviewer_model = ollama.Client(host='http://localhost:11434')
patient_model = ollama.Client(host='http://localhost:11434')

def get_interviewer_response(prompt_text: str) -> str:
    resp = interviewer_model.chat(
        model=INTERVIEWER_MODEL,
        messages=[
            {"role": "system", "content": "You are a medical psychiatrist interviewer that follows the instructions given by the user. Return ONLY JSON matching the schema."},
            {"role": "user", "content": prompt_text}
        ],
        format=ascii_schema,
        stream=False,
        options=INTERVIEWER_OPTIONS,
    )
    
    content = json.loads(resp["message"]["content"][resp["message"]["content"].rfind("{"):])["text"]
    return content

def get_patient_response(prompt_text: str) -> str:
    resp = patient_model.chat(
        model=PATIENT_MODEL,
        messages=[
            {"role": "system", "content": "You are a medical psychiatrist patient that follows the instructions given by the user. Return ONLY JSON matching the schema."},
            {"role": "user", "content": prompt_text}
        ],
        format=ascii_schema,
        stream=False,
        options=PATIENT_OPTIONS,
    )
    
    content = json.loads(resp["message"]["content"][resp["message"]["content"].rfind("{"):])["text"]
    return content

print(get_interviewer_response("Ask the patient how they are feeling today."))
print(get_patient_response("Describe your current emotional state. Act as a depressed patient. Make up a story about events leading up to a deprssive moment"))