from pydantic import BaseModel


class TouristPlace(BaseModel):
   
    nombre: str
    distancia: int
    clima: str
    altura: int 
    nivel: str


