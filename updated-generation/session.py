from state import State
import datetime
from patient import Patient
import pandas as pd


class Session:
    def __init__(self):
        self.session_id: str = datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.patient_id: int = None
        self.state: State = State()
        self.end_time: str = ""
        self.patient : Patient = None
        self.session_transcript: str = ""
        