from dto.tourist import Tourist
import uuid


class TouristService:
    def __init__(self, tourist_repository):
        self.tourist_repository = tourist_repository

    def create(self, new_tourist):
        if new_tourist.age >= 18:
            tourist = Tourist(
                id = str(uuid.uuid4()), 
                name= new_tourist.name, 
                age= new_tourist.age, 
                gender= new_tourist.gender
            )
            self.tourist_repository.create(tourist)
            return tourist 
        else:
            return {"error": "Turista menor de edad"}

    def get(self):
        return self.tourist_repository.get()

    def get_by_id(self, id: str):
        return self.tourist_repository.get_by_id(id)     


