from fastapi import FastAPI
from routes import patients, doctors, sensors, alerts, medicines

app = FastAPI(title="Smart Hospital Monitoring System API")

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(sensors.router)
app.include_router(alerts.router)
app.include_router(medicines.router)

@app.get("/")
def root():
    return {"message": "Smart Hospital Monitoring System Running"}