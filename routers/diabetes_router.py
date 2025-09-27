from fastapi import APIRouter, HTTPException
from schemas.diabetes_schemas import PatientData
from services.diabetes_services import diabetes_prediction

router = APIRouter()

@router.post("/predict")
async def predict(data: PatientData):
    try:
        prediccion = diabetes_prediction(data)
        return {"prediccion": prediccion, "modelo": data.modelo}
    except KeyError:
        raise HTTPException(status_code=400, detail="Modelo inválido. Use 'svm' o 'rf'.")
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno")
