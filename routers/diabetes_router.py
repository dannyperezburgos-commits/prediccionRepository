from fastapi import APIRouter

from schemas.diabetes_schemas import PatientData
from services.diabetes_services import diabetes_prediction


router = APIRouter()

@router.post("/predict")
async def predict(data: PatientData):
    print("datos paciente", data.identificacion_number)

    prediction = diabetes_prediction(data)

    return {"prediccion" : prediction}