class TouristPlaceRepository:
    def __init__(self, tourist_places):
        self.tourist_places = tourist_places

    def create(self, new_tourist_place):
        self.tourist_places.append(new_tourist_place)
        return new_tourist_place
    
    def get(self):
        return self.tourist_places 

    def get_by_id(self, id: str):
        for tourist_place in self.tourist_places:
            if tourist_place.id == id:
                return tourist_place
        return None