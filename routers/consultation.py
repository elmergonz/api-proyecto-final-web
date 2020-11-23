from models.consultationModel import Consultation
from models.serverResult import ServerResult
from db import dbdata

from fastapi import APIRouter

router = APIRouter()

@router.post('/api/consultation/create')
async def create(consult:Consultation, token:str):
    
    doc = await dbdata.get_doctor_by_token(token)
    
    if doc:
        if await dbdata.patient_exist(consult.patientCedula):
            
            consult['doctorEmail'] = doc['email']
            newConsult = await dbdata.add_consultation(consult)

            return ServerResult(response={
                'consulta': newConsult
            }, message="Consulta creada")
        else:
            return ServerResult(ok=False, message="El paciente no existe")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.get('/api/consultation/doctor/all')
async def get_consultation_by_doctor(token:str):

    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        consultations = await dbdata.get_consultations_by_doctor(doc['email'])

        return ServerResult(response={
            'doctor': doc['name'],
            'consultations': consultations
        }, message="Lista de consultas")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.get('/api/consultation/patient/all')
async def get_consultation_by_patient(cedula:str, token:str):

    doc = await dbdata.is_doctor_logged_in(token)

    if doc:
        consultations, patient = await dbdata.get_consultations_by_patient(cedula)

        return ServerResult(response={
            'patient': patient,
            'consultations': consultations
        }, message="Lista de consultas")
    else:
        return ServerResult(ok=False, message="Token invalido")


@router.put('/api/consultation/modify')
async def modify(consult:Consultation, consultId:str, token:str):
    
    doc = await dbdata.is_doctor_logged_in(token)

    if doc:
        if await dbdata.consultation_exist(id):

            await dbdata.update_consultation_data(consult)

            return ServerResult(message="Consulta actualizada")
        else:
            return ServerResult(ok=False, message="La consulta no existe")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.delete('/api/consultation/delete')
async def delete(consultId:str, token:str):
    
    doc = await dbdata.is_doctor_logged_in(token)

    if doc:
        if await dbdata.consultation_exist(consultId):

            await dbdata.delete_consultation(consultId)

            return ServerResult(message="Consulta eliminado")
        else:
            return ServerResult(ok=False, message="La consulta no existe")
    else:
        return ServerResult(ok=False, message="Token invalido")
