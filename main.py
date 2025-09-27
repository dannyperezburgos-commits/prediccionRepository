import numpy as np
from fastapi import FastAPI
from routers import diabetes_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(diabetes_router.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)



