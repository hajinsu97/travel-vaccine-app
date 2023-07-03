from model.vaccine import Vaccine


class VaccineList:
    def __init__(self, link: str, items: list[Vaccine.__dict__]):
        self.link = link
        self.items = items
