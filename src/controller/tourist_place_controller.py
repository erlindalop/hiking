from dto.tourist_place import TouristPlace, TouristPlaceCreate
from fastapi import APIRouter
import uuid
from service.tourist_place_service import TouristPlaceService
from fastapi import Depends

router = APIRouter()
tourist_places = []

def get_tourist_place_service():
    return TouristPlaceService(tourist_places)

@router.post("/tourist_places")
def create_turist_place(new_tourist_place: TouristPlaceCreate, tourist_place_service = Depends(get_tourist_place_service)):
    return tourist_place_service.create(new_tourist_place)


@router.get("/tourist_places")
def get_tourist_places(tourist_place_service = Depends(get_tourist_place_service)):
    return tourist_place_service.get()


@router.get("/tourist_places/{id}")
def search_id_t_places(id: str, tourist_place_service = Depends(get_tourist_place_service)):
            return tourist_place_service.get_by_id(id)
