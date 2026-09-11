from fastapi import APIRouter
from dto.tourist import TouristCreate, Tourist
import uuid
from service.tourist_service import TouristService

router = APIRouter()
tourists = []


tourist_service = TouristService()

@router.post("/tourists")
def create_tourist(new_tourist: TouristCreate):
    return tourist_service.create(new_tourist)

@router.get("/tourists")
def get_tourist():
    return tourist_service.get()
    

    
@router.get("/tourists/{id}")
def search_by_id(id: str):
    return tourist_service.get_by_id(id)
    

    