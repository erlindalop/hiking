from dto.tourist_place import TouristPlace
from fastapi import APIRouter


router = APIRouter()
tourist_places = []
@router.post("/tourist_places")
def create_turistPlace(tourist_place: TouristPlace):
    
    if len(tourist_place.nombre)> 4 :
        print('super nombre correcto')
        tourist_places.append(tourist_place)
        return tourist_place
    else:
        print('no puedes tener un nombre tan corto, revisa tu nombre por favor')


@router.get("/tourist_places")
def get_tourist_places():
    return tourist_places


@router.get("/tourist_places/{id}")
def receive_t_p(id: int):
    return (tourist_places[id])