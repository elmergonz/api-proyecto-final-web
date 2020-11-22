from pydantic import BaseModel
from typing import Optional

class Base(BaseModel):

    def __setitem__(self, key, value):
        self.__dict__[key] = value
    
    def __getitem__(self, key):
        return self.__dict__[key]

class Doctor(Base):
    name: str = ''
    email: str = ''
    password: str = ''
    
    # token:str = ''

class DoctorLog(Base):
    email: str = ''
    password: str = ''

class DoctorData(Base):
    name: Optional[str] = None
    email: Optional[str] = None
