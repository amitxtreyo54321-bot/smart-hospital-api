from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.get("/")
def get_sensors(db: Session = Depends(get_db)):
    sensors = db.query(models.SensorData).all()
    return sensors