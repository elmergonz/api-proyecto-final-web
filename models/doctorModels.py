from models.baseModel import Base

from typing import Optional

class Doctor(Base):
    name: str = ''
    email: str = ''
    password: str = ''

class DoctorLog(Base):
    email: str = ''
    password: str = ''

class DoctorData(Base):
    name: str = ''
    email: str = ''
