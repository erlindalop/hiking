from fastapi import APIRouter
from dto.tourist import TouristCreate, Tourist
import uuid
from repository.tourist_repository import TouristRepository
from service.tourist_service import TouristService
from fastapi import Depends

router = APIRouter()

tourists = []
def get_tourist_service():
    tourist_repository = TouristRepository(tourists)
    return TouristService(tourist_repository)

@router.post("/tourists")
def create_tourist(new_tourist: TouristCreate, tourist_service = Depends(get_tourist_service)):
    print("Turista creado a")
    return tourist_service.create(new_tourist)

@router.get("/tourists")
def get_tourist(tourist_service = Depends(get_tourist_service)):
    return tourist_service.get()
    

    
@router.get("/tourists/{id}")
def search_by_id(id: str, tourist_service = Depends(get_tourist_service)):
    return tourist_service.get_by_id(id)
    

    