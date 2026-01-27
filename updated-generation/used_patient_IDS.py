"""
Docstring for updated-generation.used_patient_IDS

format:
same index in array

"""
import pandas as pd

def append_ID(patient_ID = None, session_ID = None):
    df = pd.read_csv("used_patient_IDS.csv")
    df.loc[len(df)] = {"patient_ID": patient_ID, "session_ID": session_ID}
    df.to_csv("used_patient_IDS.csv", index=False)
    
def get_patient_IDS():
    df = pd.read_csv("used_patient_IDS.csv")
    patient_IDS = df["patient_ID"].tolist()
    return patient_IDS

def get_session_IDS():
    df = pd.read_csv("used_patient_IDS.csv")
    session_IDS = df["session_ID"].tolist()
    return session_IDS