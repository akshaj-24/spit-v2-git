import numpy as np
import pandas as pd
import ollama

class Patient:
    def __init__(self):
        self.patient_ID = None
        self.row: pd.DataFrame = None
        self.name = None
        self.age = None
        self.gender = None
        self.marital_status = None
        self.education = None
        self.occupation = None
        self.context = None
        
        
    def update_patient_data(self):
        if self.row is None:
            return
        self.patient_ID = int(self.row['patient_ID'].values[0])
        self.name = str(self.row['patient_name'].values[0])
        self.age = int(self.row['patient_age'].values[0])
        self.gender = str(self.row['patient_gender'].values[0])
        self.marital_status = str(self.row['patient_marital_status'].values[0])
        self.education = str(self.row['patient_education'].values[0])
        self.occupation = str(self.row['patient_occupation'].values[0])
        self.context = str(self.row['patient_context'].values[0])
        return
    