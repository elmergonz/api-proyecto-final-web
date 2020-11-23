from models import doctorModels, patientModel, consultationModel
from deta import Deta
import os

deta = Deta(os.getenv('DETA_PROJECT_KEY'))

dbDoctors = deta.Base('users')
dbPatients = deta.Base('patients')
dbConsultations = deta.Base('consultations')

# ------ doctor actions

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
        key: value for key, value in doctor if value
    }, key=doctor.email)

async def update_doctor_password(email:str, newPassword:str):
    dbDoctors.update({
        'password': newPassword
    }, key=email)

async def get_doctor(doctor:doctorModels.DoctorLog):
    # El formato en que son devueltos los datos es una lista como esta: [{datos...}, {datos...}, ...]
    
    doc = next(dbDoctors.fetch({
        key: value for key, value in doctor
    }))

    # retornara el primer elmento si la lista no esta vacia, sino solo devolvera la alista vacia
    return doc[0] if doc else doc

async def get_doctor_by_email(email:str):
    return dbDoctors.get(email)

async def get_doctor_by_token(token:str):
    doc = next(dbDoctors.fetch({
        'token': token
    }))

    return doc[0] if doc else doc

async def is_doctor_logged_in(token:str):
    doc = next(dbDoctors.fetch({
        'token': token
    }))

    return True if doc else False

# ------ patient actions

async def add_patient(patient:patientModel.Patient):
    newPatient = dbPatients.put({
        key: value for key, value in patient
    }, key=patient.cedula)

    return newPatient

async def update_patient_data(patient:patientModel.Patient):
    dbPatients.update({
        key: value for key, value in patient if value
    }, key=patient.cedula)

async def get_patients(email:str):
    return next(dbPatients.fetch({'doctorEmail': email}))

async def get_patient_by_cedula(cedula:str):
    return dbPatients.get(cedula)

async def patient_exist(cedula:str):
    return True if dbPatients.get(cedula) else False

async def delete_patient(cedula:str):
    return dbPatients.delete(cedula)

# ------ consultation actions

async def add_consultation(consult:consultationModel.Consultation):
    newConsult = dbConsultations.put({
        key: value for key, value in consult
    })

    return newConsult

async def update_consultation_data(consult:consultationModel.Consultation):
    dbConsultations.update({
        key: value for key, value in consult if value
    })

async def get_consultations_by_doctor(doctorEmail:str):
    return next(dbConsultations.fetch({'doctorEmail': doctorEmail}))

async def get_consultations_by_patient(cedula:str):
    return next(dbConsultations.fetch({'paritentCedula': cedula})), await get_patient_by_cedula(cedula)

async def consultation_exist(key:str):
    return True if dbConsultations.get(key) else False

async def delete_consultation(id:str):
    return dbConsultations.delete(id)
