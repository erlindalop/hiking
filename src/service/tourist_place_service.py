from dto.tourist_place import TouristPlace, TouristPlaceCreate
import uuid


class TouristPlaceService:
    def __init__(self, tourist_places):
        self.tourist_places = tourist_places

    def create(self, new_tourist_place: TouristPlaceCreate):
        if len(new_tourist_place.nombre)> 4 :
            tourist_place = TouristPlace( 
                id = str(uuid.uuid4()),
                nombre= new_tourist_place.nombre,
                distancia= new_tourist_place.distancia,
                clima= new_tourist_place.clima,
                altura= new_tourist_place.altura,
                nivel= new_tourist_place.nivel,
            )
            self.tourist_places.append(tourist_place)
            return tourist_place
        else:
            return {'no puedes tener un nombre tan corto, revisa tu nombre por favor'}

    def get(self):
        return self.tourist_places

    def get_by_id(self, id: str):
        for tourist_place in self.tourist_places:
            if tourist_place.id == id:
                return tourist_place