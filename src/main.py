from fastapi import FastAPI
from controller.tourist_controller import router as tourist_router
from controller.tourist_place_controller import router as tourist_place_router


app = FastAPI()

app.include_router(tourist_router)
app.include_router(tourist_place_router)
