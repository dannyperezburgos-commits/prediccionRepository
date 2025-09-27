from fastapi import APIRouter, HTTPException
from schemas.diabetes_schemas import PatientData
from services.diabetes_services import diabetes_prediction

router = APIRouter()

@router.post("/predict")
async def predict(data: PatientData):
    try:
        return {"prediccion": diabetes_prediction(data), "modelo": data.modelo}
    except KeyError:
        raise HTTPException(status_code=400, detail="Modelo inválido")
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno")
