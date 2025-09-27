from pydantic import BaseModel

class PatientData(BaseModel):
    n: int
    p: int
    k: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    label: str