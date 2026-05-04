from sqlalchemy.orm import Session
import models


# Patients
def create_patient(db: Session, patient):
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def get_patients(db: Session):
    return db.query(models.Patient).all()


# Doctors
def create_doctor(db: Session, doctor):
    new_doctor = models.Doctor(**doctor.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


def get_doctors(db: Session):
    return db.query(models.Doctor).all()


# Medicines
def create_medicine(db: Session, medicine):
    new_medicine = models.Medicine(**medicine.dict())
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return new_medicine


def get_medicines(db: Session):
    return db.query(models.Medicine).all()