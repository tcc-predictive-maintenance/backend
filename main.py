from fastapi import FastAPI

from src.model.machine_description_dto import MachineDescriptionDTO
from src.service.predict_service import predict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Predictive Maintenance API is running"}


@app.post("/predict")
async def predict_request(machine_description: MachineDescriptionDTO):
    return predict(machine_description)
