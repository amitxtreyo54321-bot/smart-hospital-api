from pydantic import BaseModel


# --------------------
# Patient Schemas
# --------------------

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    disease: str


class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    disease: str

    class Config:
        from_attributes = True


# --------------------
# Doctor Schemas
# --------------------

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: str


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    email: str

    class Config:
        from_attributes = True


# --------------------
# Sensor Schemas
# --------------------

class SensorCreate(BaseModel):
    patient_id: int
    heart_rate: int
    temperature: float
    oxygen_level: int


class Sensor(BaseModel):
    id: int
    patient_id: int
    heart_rate: int
    temperature: float
    oxygen_level: int

    class Config:
        from_attributes = True


# --------------------
# Medicine Schemas
# --------------------

class MedicineCreate(BaseModel):
    patient_id: int
    medicine_name: str
    dosage: str


class Medicine(BaseModel):
    id: int
    patient_id: int
    medicine_name: str
    dosage: str

    class Config:
        from_attributes = True