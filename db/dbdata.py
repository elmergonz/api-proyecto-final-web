from models import doctorModels, patientModel, consultationModel
from deta import Deta
import os

deta = Deta(os.getenv('DETA_PROJECT_KEY'))

dbDoctors = deta.Base('users')
dbPatients = deta.Base('patients')
dbConsultations = deta.Base('consultations')

# doctor actions

async def add_doctor(doctor:doctorModels.Doctor):
    newDoctor = dbDoctors.put({
        key: value for key, value in doctor
    }, key=doctor.email)

    return newDoctor

async def update_doctor_token(email:str, token:str):
    dbDoctors.update({
        'token': token
    }, key=email)

async def update_doctor_data(doctor:doctorModels.DoctorData):
    dbDoctors.update({
        key: value for key, value in doctor
    }, key=doctor.email)

async def update_doctor_password(email:str, newPassword:str):
    dbDoctors.update({
        'password': newPassword
    }, key=email)

async def get_doctor(doctor:doctorModels.DoctorLog):
    # El formato en que son devueltos los datos es una lista como esta: [{datos...}, {datos...}, ...]
    
    return next(dbDoctors.fetch({
        key: value for key, value in doctor
    }))[0] # El '0' es solo para que me devuelva el primer valor

async def get_doctor_by_email(email:str):
    return dbDoctors.get(email)

async def get_doctor_by_token(token:str):
    return next(dbDoctors.fetch({
        'token': token
    }))[0]

