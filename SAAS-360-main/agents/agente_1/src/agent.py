from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "agente_1 healthy"}