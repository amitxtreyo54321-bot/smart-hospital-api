from sqlalchemy import Column, Integer, String, Float
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(10))
    disease = Column(String(100))


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    specialization = Column(String(100))
    email = Column(String(100))


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    heart_rate = Column(Integer)
    temperature = Column(Float)
    oxygen_level = Column(Integer)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    alert_message = Column(String(255))


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    medicine_name = Column(String(100))
    dosage = Column(String(50))

class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer)
    bed_number = Column(Integer)
    status = Column(String(50))
