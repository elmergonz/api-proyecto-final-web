from models.doctorModels import Doctor, DoctorData, DoctorLog
from models.serverResult import ServerResult
from db import dbdata

from fastapi import APIRouter
import secrets
import re

router = APIRouter()

@router.post('/api/doctor/register')
async def register(doctor:Doctor):

    doc = await dbdata.get_doctor_by_email(doctor.email)

    if not doc:
        if not check_email(doctor.email):
            return ServerResult(ok=False, message="Agrege una direccion de correo valida")
        
        doctor['token'] = secrets.token_urlsafe(20)

        newDoctor = await dbdata.add_doctor(doctor)

        # Si se creo correctamente...
        if newDoctor:
            return ServerResult(response={
                'token': doctor['token']
            }, message="Doctor creado correctamente")
    else:
        return ServerResult(ok=False, message="Este doctor ya existe")



def check_email(email:str):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return True
    return False
