from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from routers import user

import uvicorn

app = FastAPI(
    title='medicos',
    verson='1.0',
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(user, tags=['User'])

@app.get('/api', tags=['Inicio'])
async def get_root():
    return {
        'api': 'proyecto final :D',
        'docs': 'https://dj21vc.deta.dev' + app.docs_url
    }

if __name__ == "__main__":
    
    uvicorn.run(app)