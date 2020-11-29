from models.patientModel import Patient
from models.serverResult import ServerResult
from packages.checks import check_email
from db import dbdata

from fastapi import APIRouter
import base64
import requests

router = APIRouter()

url_api_cedula = 'https://api.adamix.net/apec/cedula/'
url_api_foto = 'https://api.adamix.net/apec/foto2/'

async def get_cedula_data(cedula:str):
    return requests.get(url_api_cedula + cedula).json()

async def get_foto(cedula:str):
    foto = requests.get(url_api_foto + cedula).content

    return str(base64.b64encode(foto))

@router.post('/api/patient/register')
async def register(patient:Patient, token:str):

    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        if not await dbdata.patient_exist(patient.cedula, doc['email']):
            patient_data = await get_cedula_data(patient.cedula)

            if patient_data['ok']:
                patient['name'] = patient_data['Nombres']
                patient['lastname'] = patient_data['Apellido1'] + ' ' + patient_data['Apellido2']
                patient['gender'] = patient_data['IdSexo']
                patient['birthdate'] = patient_data['FechaNacimiento']

                if not patient['foto']:
                    patient['foto'] = await get_foto(patient.cedula)
            else:
                return ServerResult(ok=False, message="La cedula que ha ingresado no es valida")

            if not check_email(patient.email):
                return ServerResult(ok=False, message="Agrege una direccion de correo valida")

            patient['doctorEmail'] = doc['email']
            patient['bloodType'] = patient['bloodType'].upper()

            newPatient = await dbdata.add_patient(patient)

            # Si se creo correctamente...
            if newPatient:
                return ServerResult(response={
                    'paciente': newPatient
                }, message="Paciente creado correctamente")
        else:
            return ServerResult(ok=False, message="Este paciente ya existe")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.get('/api/patient/all')
async def get_patients(token:str):

    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        patients = await dbdata.get_patients(doc['email'])

        return ServerResult(response={
            'doctor': doc['name'],
            'pacientes': patients
        }, message="Lista de pacientes")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.put('/api/patient/modify')
async def modify(patient:Patient, token:str):
    
    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        pat = await dbdata.get_patient_by_cedula(patient.cedula, doc['email'])
        if pat:
            patient['key'] = pat['key']
            patient['bloodType'] = patient['bloodType'].upper()

            await dbdata.update_patient_data(patient)

            return ServerResult(message="Paciente actualizado")
        else:
            return ServerResult(ok=False, message="El paciente no existe")
    else:
        return ServerResult(ok=False, message="Token invalido")

@router.delete('/api/patient/delete')
async def delete(cedula:str, token:str):

    doc = await dbdata.get_doctor_by_token(token)

    if doc:
        pat = await dbdata.get_patient_by_cedula(cedula, doc['email'])
        if pat:

            await dbdata.delete_patient(pat['key'])

            return ServerResult(message="Paciente eliminado")
        else:
            return ServerResult(ok=False, message="El paciente no existe")
    else:
        return ServerResult(ok=False, message="Token invalido")
