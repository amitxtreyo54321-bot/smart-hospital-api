from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/")
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).all()
    return alerts