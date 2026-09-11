from dto.tourist import Tourist
import uuid

tourists = []

class TouristService:
    def create(self, new_tourist):
        if new_tourist.age >= 18:
            tourist = Tourist(
                id = str(uuid.uuid4()), 
                name= new_tourist.name, 
                age= new_tourist.age, 
                gender= new_tourist.gender
            )
            tourists.append(tourist)
            return tourist 
        else:
            return {"error": "Turista menor de edad"}

    def get(self):
        return tourists

    def get_by_id(self, id: str):
        for tourist in tourists:
            if tourist.id == id:
                return tourist
