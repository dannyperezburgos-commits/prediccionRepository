import pickle
import numpy as np
from pathlib import Path
from schemas.diabetes_schemas import PatientData

LABELS = [
    'rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean',
    'blackgram','lentil','pomegranate','banana','mango','grapes','watermelon',
    'muskmelon','apple','orange','papaya','coconut','cotton','jute','coffee'
]

MODELOS = {
    'svm': pickle.load(Path('CropRecommendationSVNV1.pkl').open('rb')),
    'rf':  pickle.load(Path('CropRecommendationRandomV1.pkl').open('rb')),
}

def diabetes_prediction(data: PatientData):
    xin = np.array([
        data.n,
        data.p,
        data.k,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]).reshape(1, 7)

    prediction = MODELOS[data.modelo].predict(xin)
    return LABELS[int(prediction[0])]
