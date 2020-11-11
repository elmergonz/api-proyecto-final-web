from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return {
        'api': 'proyecto final :D',
        'docs': app.docs_url
    }