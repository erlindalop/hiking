from pydantic import BaseModel


class TouristPlaceCreate(BaseModel):
   
    nombre: str
    distancia: int
    clima: str
    altura: int 
    nivel: str 


class TouristPlace(BaseModel):
    id: str
    nombre: str
    distancia: int
    clima: str
    altura: int 
    nivel: str 

