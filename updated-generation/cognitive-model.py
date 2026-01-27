class CM:
    def __init__(self, patient_ID: int, conversational_styles: list[str], core_beliefs: list[str], situation: str, intermediate_beliefs: str, automatic_thoughts: str):
        self.patient_ID = patient_ID
        self.conversational_styles = conversational_styles
        self.core_beliefs = core_beliefs
        self.situation = situation
        self.intermediate_beliefs = intermediate_beliefs
        self.automatic_thoughts = automatic_thoughts