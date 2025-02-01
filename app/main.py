from fastapi import FastAPI
from app.automation import execute_playbook

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SOC Automation API Running"}

@app.post("/run-playbook/")
def run_playbook(playbook: str):
    result = execute_playbook(f"ansible_playbooks/{playbook}.yml")
    return {"status": result}
