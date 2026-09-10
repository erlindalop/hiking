from pydantic import BaseModel


class TouristCreate(BaseModel):
   
    name: str
    age: int
    gender:str
    

class Tourist(BaseModel):
    id: str
    name: str
    age: int
    gender: str