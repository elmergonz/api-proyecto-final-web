from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    idNumber: str = '' # cedula
    name: str = ''
    lastname: str = ''
    gender: str = ''
    birthDate: str = ''

    # -- optionals: Estas son las caracteristicas que se pueden editar  --

    foto: Optional[str] = None
    email: Optional[str] = None
    bloodType: Optional[str] = None
    alergias: Optional[str] = None
