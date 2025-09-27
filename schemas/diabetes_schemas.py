from pydantic import BaseModel

class PatientData(BaseModel):
    first_name: str
    last_name: str
    identificacion_number: int
    pregnancies: int
    glucose: int
    bloodpressure: int
    skinthickness: int
    insulin: int
    bmi: float
    diabetespedigreefunction: float
    age: int
    outcome: int