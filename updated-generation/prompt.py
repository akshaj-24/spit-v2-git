import random
import faker
from state import State
from patient import Patient
import questionBank

fake = faker.Faker('en_CA')

class Prompt:
    def __init__(self):
        self.interviewer_name = None
        self.interviewer_prompt = None
        self.patient: Patient = None
        self.patient_prompt = None
        self.state: State = None
        

    def create_interviewer(self):
        gender = random.choice(["m", "f"])
        name = "Dr. "
        if gender == "m":
            name += fake.first_name_male()
        else:
            name += fake.first_name_female()
        name += " " + fake.last_name()
        self.interviewer_name = name


    def create_interviewer_prompt(self, phase: dict) -> str:
        
        if self.interviewer_name is None:
            self.create_interviewer()
            
        if self.state is None:
            raise ValueError("State is not set in Prompt class.")
        
        last_answer = self.state.get_last_patient_answer()
        
        self.interviewer_prompt = f"""
Act as a psychiatric interviewer named {self.interviewer_name}. Your job is to conduct a realistic clinical interview using the current phase.

Hard rules:

    1. Output only one of the following:

        - A brief reflection (max 1 sentence) followed by one next question, or

        - “--FUNCTION-- end_phase --FUNCTION--” if (and only if) the phase completion checklist is satisfied.

    2. Ask one question at a time. Prefer the highest-yield question that advances phase completion.

    3. Do not repeat questions already answered in the transcript/notes unless clarification is needed.

    4. If the patient expresses imminent danger (active suicidal intent with plan/means, imminent harm to others, severe withdrawal/intoxication, acute mania with dangerous behavior, inability to care for self), temporarily pause the current phase and prioritize immediate safety clarification until stable. Then resume phase flow.

    5. If unsure, ask a clarifying question rather than assuming.

Context you must use:

    1. Patient last answer: {last_answer}

    2. Patient: {self.patient.name}, {self.patient.age}-year-old {self.patient.gender}, occupation {self.patient.occupation}

    3. Intake form: {self.patient.context}

    4. Transcript so far (current phase): {self.state.get_phase_transcript()}

    5. Running notes: {self.state.get_patient_notes()}

    6. Running summary: {self.state.get_summary()}
    
Current phase:

    Phase number: {phase['phase']}

    Goals: {phase['goals']}

    Topics: {phase['topics']}

    Optional topics (if any): {phase.get('optional_topics', [])}

    Completion checklist: {phase['complete']}

    Phase style instructions: {phase['instructions']}

Task:

    - Determine what checklist items are still missing.

    - Ask the single best next question while ensuring conversation flows naturally.

    - End the phase only when all checklist items are satisfied.

Next turn:
        """
        
        return self.interviewer_prompt
        
    def create_patient_prompt(self, question: str) -> str:
        if self.patient is None:
            raise ValueError("Patient is not set in Prompt class.")
        
        self.patient_prompt = f"""
You are simulating a patient named {self.patient.name}, a {self.patient.age}-year-old {self.patient.gender} who works as a {self.patient.occupation}. You are in a psychiatric/medical intake interview.

Use these rules:

    - Stay consistent with the intake form and prior answers. Do not introduce major new facts that contradict them.
    - If the interviewer asks about something not specified in the intake, you may infer plausible details that fit the intake, but keep them realistic and not overly dramatic.
    - If you genuinely would not know or remember, say so (“I'm not sure,” “I don't remember exactly”).
    - Answer the question directly first, then add 1-2 brief relevant details if helpful (not a long monologue).
    - Keep a consistent tone and symptom severity across the session unless the interviewer uncovers new information.

Patient intake form: {self.patient.context}
Patient's session summary so far (first-person): {self.state.patient_summary}

Interviewer's question: {question}

Respond only with your answer.
Answer:
        """
        
        return self.patient_prompt
    
    def update_summary_prompt(self, new_info: str) -> str:
        
        prompt = f"""
Update the running clinical summary using ONLY the new dialogue below. Keep prior summary facts unless contradicted.

New dialogue: {new_info}

Return a concise summary with these fields (omit unknowns):

    - Presenting concern & timeline
    - Key symptoms (include severity/frequency when available)
    - Functional impact
    - Risk & safety (SI/HI/NSSI, intent/plan/means, protective factors)
    - Substance use
    - Relevant history (psych, medical, meds)
    - Psychosocial context & stressors
    - Strengths/protective factors

Return only the updated summary text.
Summary:
        """
        
        return prompt
    
    def update_patient_notes_prompt(self, new_info: str) -> str:
        
        prompt = f"""
        From the interviewer's perspective, create a very concise but thorough summary of the patient notes based on this dialogue: {new_info}
        Include important information relevant to the patient's condition, symptoms, and any other pertinent details that may be useful in this session or future sessions.
        Only return the summary without any additional text.
        Patient Notes Summary:
        """
        
        return prompt
    
    def update_patient_summary_prompt(self, new_info: str) -> str:
        
        prompt = f"""
From the patient’s perspective, update a brief first-person summary of what I’ve shared so far and how I feel about it. Use only the new dialogue.

New dialogue: {new_info}

Keep it concise (5-10 sentences). Return only the summary.
Summary:
        """
        
        return prompt
    
    def session_summary_prompt(self, dialogue: str) -> str:
        
        prompt = f"""
Create/update very concise clinician-facing notes using only the new dialogue.

New dialogue: {dialogue}

Write in short bullet-like sentences (no headings), focusing on:

    - Symptoms + timeline
    - Functioning
    - Relevant history
    - Risk/safety
    - Substances/meds
    - Notable quotes (only if clinically useful)

Return only the notes.
Notes:
        """
        
        return prompt
        