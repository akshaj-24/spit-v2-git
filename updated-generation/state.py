from os import path
import pandas as pd
from pathlib import Path

class State:
    def __init__(self):
        self.current_phase: int = 1
        self.phase_transcript: str = ""                                         # Path to current phase transcript
        self.patient_notes: str = "First phase, No notes yet."                  # Accumulated patient notes
        self.summary: str = "First phase, No summary yet."                      # Running summary of the session
        self.patient_summary: str = "First phase, No patient summary yet."      # Summary for patient model

    def get_current_phase(self) -> int:
        return self.current_phase

    def next_phase(self):
        self.current_phase += 1

    def add_to_phase_transcript(self, role: str, content: str):
        pt = pd.read_json(self.phase_transcript, lines=True)
        pt.loc[len(pt)] = [role, content]
        pt.to_json(self.phase_transcript, orient="records", lines=True)

    def reset_phase_transcript(self):
        df = pd.DataFrame(columns=["role", "content"])
        df.to_json(self.phase_transcript, orient="records", lines=True)
        row = pd.DataFrame([{"role": "system", "content": f"---"}])

        row.to_json(self.phase_transcript, orient="records", lines=True)
        return 1

    def get_phase_transcript(self):
        df = pd.read_json(self.phase_transcript, lines=True)
        dialogue = "\n".join([f"{row['role']}: {row['content']}" for index, row in df.iterrows()])
        return dialogue

    def update_patient_notes(self, new_notes: str):
        self.patient_notes += "\n" + new_notes
        return 1

    def get_patient_notes(self):
        return self.patient_notes

    def reset_patient_notes(self):
        self.patient_notes = ""
        return 1

    def get_summary(self):
        return self.summary

    def update_summary(self, new_summary: str):
        self.summary += "\n" + new_summary
        return 1

    def reset_summary(self):
        self.summary = ""
        return 1

    def get_patient_summary(self):
        return self.patient_summary

    def update_patient_summary(self, new_summary: str):
        self.patient_summary += "\n" + new_summary
        return 1

    def reset_patient_summary(self):
        self.patient_summary = ""
        return 1

    def reset_all(self):
        self.reset_phase_transcript()
        self.reset_patient_notes()
        self.reset_summary()
        self.reset_patient_summary()
        self.current_phase = "1"
        return 1
    
    def get_last_patient_answer(self) -> str:
        
        path = Path(self.phase_transcript)
        if not path.exists() or path.stat().st_size == 0:
            return ""
        
        
        df = pd.read_json(self.phase_transcript, lines=True)  # JSONL [web:21]
        
        if "role" not in df.columns or "content" not in df.columns:
            return ""
        
        
        s = df.loc[df["role"].eq("patient"), "content"]        # boolean filter [web:53]
        
        
        
        return s.iloc[-1] if not s.empty else ""               # last element [web:45]
