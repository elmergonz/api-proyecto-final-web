from models.patientModel import Patient

from pydantic import BaseModel
from typing import Optional

class Consultation(BaseModel):
    patient: Patient = None
    insuranceNumber: str = ''
    date: str = ''
    amount: float = ''

    # -- optionals: Estas son las caracteristicas que se pueden editar  --

    reason: Optional[str] = None
    diagnose: Optional[str] = None
    note: Optional[str] = None
    foto: Optional[str] = None
