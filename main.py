from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from routers import doctor, patient, consultation

import uvicorn

app = FastAPI(
    title='api medicos',
    verson='1.0',
    docs_url='/docs',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(doctor.router, tags=['Doctor'])
app.include_router(patient.router, tags=['Patient'])
app.include_router(consultation.router, tags=['Consultation'])

@app.get('/', tags=['Home'])
@app.get('/api', tags=['Home'])
async def get_root():
    return {
        'api': 'proyecto final :D',
        'docs': 'https://dgon3z.deta.dev' + app.docs_url
    }

if __name__ == "__main__":
    
    uvicorn.run('main:app', reload=True)
