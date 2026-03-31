from fastapi import FastAPI
import yaml

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset"}

@app.post("/step")
def step(action: dict):
    return {
        "state": {},
        "reward": 0.5,
        "done": False,
        "info": {}
    }

@app.get("/")
def root():
    return {"message": "OpenEnv running"}