from fastapi import APIRouter
from dto.tourist import TouristCreate, Tourist
import uuid

router = APIRouter()
tourists = []

@router.post("/tourists")
def create_tourist(tourist_create: TouristCreate):

    if tourist_create.age >= 18:
        tourist = Tourist(
            id = str(uuid.uuid4()), 
            name= tourist_create.name, 
            age= tourist_create.age, 
            gender= tourist_create.gender
        )
        tourists.append(tourist)
        return tourist 
    else:
        return {"error": "Turista menor de edad"}


@router.get("/tourists")
def get_tourist():
    return tourists
   
@router.get("/tourists/{id}")
def receive(id: str):
    # buscar un turista con el id en turistas, devolver el que coincida. 
    pass
    