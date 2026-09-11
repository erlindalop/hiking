from dto.tourist_place import TouristPlace, TouristPlaceCreate
from fastapi import APIRouter
import uuid


router = APIRouter()
tourist_places = []



@router.post("/tourist_places")
def create_turist_place(new_tourist_place: TouristPlaceCreate):
    if len(new_tourist_place.nombre)> 4 :
        tourist_place = TouristPlace( 
            id = str(uuid.uuid4()),
            nombre= new_tourist_place.nombre,
            distancia= new_tourist_place.distancia,
            clima= new_tourist_place.clima,
            altura= new_tourist_place.altura,
            nivel= new_tourist_place.nivel,
        )
        tourist_places.append(tourist_place)
        return tourist_place
    else:
         return {'no puedes tener un nombre tan corto, revisa tu nombre por favor'}


@router.get("/tourist_places")
def get_tourist_places():
    return tourist_places


@router.get("/tourist_places/{id}")
def search_id_t_places(id: str):
    for tourist_place in tourist_places:
        if tourist_place.id == id:
            return tourist_place
