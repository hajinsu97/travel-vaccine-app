from model.dosage import Dosage

class DosageList:
    def __init__(self, disease: str, items: list[Dosage]):
        self.disease = disease
        self.items = items
