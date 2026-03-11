from fastapi import FastAPI
from planner import build_plan
from registry import get_registry

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/plan")
def create_plan():
    return build_plan()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)