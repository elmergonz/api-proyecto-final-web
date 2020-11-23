from models.doctorModels import Doctor, DoctorData, DoctorLog
from models.serverResult import ServerResult
from packages.checks import check_email
from db import dbdata

from fastapi import APIRouter
import secrets

router = APIRouter()

def generate_token():
    return secrets.token_urlsafe(20)

@router.post('/api/doctor/register')
async def register(doctor:Doctor):

    doc = await dbdata.get_doctor_by_email(doctor.email)

    if not doc:
        if not check_email(doctor.email):
            return ServerResult(ok=False, message="Agrege una direccion de correo valida")
        
        doctor['token'] = generate_token()

        newDoctor = await dbdata.add_doctor(doctor)

        # Si se creo correctamente...
        if newDoctor:
            return ServerResult(response={
                'token': doctor['token']
            }, message="Doctor creado correctamente")
    else:
        return ServerResult(ok=False, message="Este doctor ya existe")

@router.post('/api/doctor/login')
async def login(doctor:DoctorLog):
    
    doc = await dbdata.get_doctor(doctor)
    emailExist = True if await dbdata.get_doctor_by_email(doctor.email) else False

    if doc:
        if doc['token']:
            return ServerResult(response={
                'token': doc['token']
            }, message="Su sesion ya estaba iniciada")

        token = generate_token()
        dbdata.update_doctor_token(doc['email'], token)

        return ServerResult(response={
            'token': token
        }, message="Sesion iniciada correctamente")
    elif not emailExist:
        return ServerResult(ok=False, message="Este correo electronico no existe")
    else:
        return ServerResult(ok=False, message="Contraseña incorrecta")

@router.post('/api/doctor/logout')
async def logout(token:str):
    
    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        dbdata.update_doctor_token(doc['email'], '')

        return ServerResult(message="Sesion cerrada")
    else:
        return ServerResult(ok=False, message="Token invalido")
