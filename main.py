from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.model.machine_description_dto import MachineDescriptionDTO
from src.service.predict_service import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Predictive Maintenance API is running"}


@app.post("/predict")
async def predict_request(machine_description: MachineDescriptionDTO):
    return predict(machine_description)
