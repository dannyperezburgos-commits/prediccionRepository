from pydantic import BaseModel
from typing import Literal

class PatientData(BaseModel):
    n: int
    p: int
    k: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    modelo: Literal['svm', 'rf']
    label: str | None = None
