from dto.tourist_place import TouristPlace, TouristPlaceCreate
import uuid


class TouristPlaceService:
    def __init__(self, tourist_places_repository):
        self.tourist_place_repository = tourist_places_repository

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
            self.tourist_place_repository.create(tourist_place)
            return tourist_place
        else:
            return {'no puedes tener un nombre tan corto, revisa tu nombre por favor'}

    def get(self):
        return self.tourist_place_repository.get()

    def get_by_id(self, id: str):
        return self.tourist_place_repository.get_by_id(id)  