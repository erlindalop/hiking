class TouristRepository:

    def __init__(self, tourists):
        self.tourists = tourists

    def create(self, new_tourist):
        self.tourists.append(new_tourist)

    def get(self):
        return self.tourists

    def get_by_id(self, id: str):
        for tourist in self.tourists:
            if tourist.id == id:
                return tourist
        return None
