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
        self.state = None
        

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
        Act as a medical interviewer named {self.interviewer_name}. You are conducting a medical interview with a patient. Use the following context to guide your questions and responses.
        Patient's last answer: {last_answer}
        Use the following phase information to guide your questions:
        Goals: {phase['goals']}
        Topics to cover: {phase['topics']}
        Mark complete when this info is collected: {phase['complete']}. To mark complete simply return this text "--FUNCTION-- end_phase --FUNCTION--" when the phase is complete.
        Phase instructions: {phase['instructions']}
        
        Patient intake form: {self.patient.context}
        
        Current transcript so far:
        {self.state.get_phase_transcript()}
        
        Notes and summary so far:
        Patient Notes: {self.state.get_patient_notes()}
        Patient Summary: {self.state.get_summary()}
        
        You can ask as many questions as needed to complete the phase goals. When done with the phase, respond with "--FUNCTION-- end_phase --FUNCTION--".
        Only respond with your next question or "--FUNCTION-- end_phase --FUNCTION--" if the phase is complete.
        Question:
        """
        
        return self.interviewer_prompt
        
    def create_patient_prompt(self, question: str) -> str:
        if self.patient is None:
            raise ValueError("Patient is not set in Prompt class.")
        
        self.patient_prompt = f"""
        You are a patient named {self.patient.name}, a {self.patient.age}-year-old {self.patient.gender} working as a {self.patient.occupation}. You are here for a medical interview. Use the following context to answer the interviewer's questions.
        Patient intake form: {self.patient.context}
        
        Answer the interviewer's question as accurately as possible based on your context. You can provide additional relevant details to help the interviewer understand your situation better. You do not need to be elaborate beyond what is necessary to answer the question.
        
        Interviewer's Question: {question}
        
        Respond only with your answer to the question.
        Answer:
        """
        
        return self.patient_prompt
    
    def update_summary_prompt(self, new_info: str) -> str:
        
        prompt = f"""
        Create a very concise but thorough summary of the conversation based on this dialogue: {new_info}
        
        Only return the summary without any additional text.
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
        From the patient's perspective, create a concise summary of this session's conversation based on this dialogue: {new_info}
        Focus on the patient's feelings, concerns, and overall experience during the interview. Write in first person as if you are the patient.
        Only return the summary without any additional text.
        Summary:
        """
        
        return prompt
    
    def session_summary_prompt(self, dialogue: str) -> str:
        
        prompt = f"""
        Create a comprehensive summary of the entire session based on this dialogue: {dialogue}
        Include key points discussed, important patient information, and any conclusions or next steps.
        Be concise but thorough.
        
        Return the summary in this format: {questionBank.summary}
        
        Only return the summary without any additional text.
        Session Summary:
        """
        
        return prompt
        