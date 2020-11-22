from pydantic import BaseModel
from typing import Optional

class Doctor(BaseModel):
    name: str = ''
    email: str = ''
    password: str = ''

class DoctorLog(BaseModel):
    email: str = ''
    password: str = ''

class DoctorData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
