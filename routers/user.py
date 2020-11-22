from fastapi import APIRouter
from models.userModels import *

router = APIRouter()

@router.post('/api/doctor/register')
async def register(doctor:Doctor):


    return {

    }