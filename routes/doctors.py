from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/doctors", tags=["Doctors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@router.get("/")
def read_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)
