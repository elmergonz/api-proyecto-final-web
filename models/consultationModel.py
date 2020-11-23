from models.patientModel import Patient

from pydantic import BaseModel
from typing import Optional

class Consultation(BaseModel):
    patientCedula: str = ''
    insuranceNumber: str = '' # numero de seguro
    date: str = ''
    amount: float = 0.0

    # -- optionals: Estas son las caracteristicas que se deberian editar  --

    reason: str = ''
    diagnose: str = ''
    note: str = ''
    foto: str = ''
