from models import *
from deta import Deta
import os

deta = Deta(os.getenv("DETA_PROJECT_KEY"))

dbUsers = deta.Base('users')
dbPatients = deta.Base('patients')
dbConsultations = deta.Base('consultations')

