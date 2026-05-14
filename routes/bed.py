from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Bed
from schemas import BedCreate, BedUpdate

router = APIRouter()

# ======================
# CREATE BED
# ======================

@router.post("/beds")
def create_bed(data: BedCreate, db: Session = Depends(get_db)):

    new_bed = Bed(
        room_id=data.room_id,
        bed_number=data.bed_number,
        status=data.status
    )

    db.add(new_bed)
    db.commit()
    db.refresh(new_bed)

    return new_bed


# ======================
# GET ALL BEDS
# ======================

@router.get("/beds")
def get_beds(db: Session = Depends(get_db)):

    beds = db.query(Bed).all()

    return beds


# ======================
# GET SINGLE BED
# ======================

@router.get("/beds/{id}")
def get_single_bed(id: int, db: Session = Depends(get_db)):

    bed = db.query(Bed).filter(Bed.id == id).first()

    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")

    return bed


# ======================
# UPDATE BED
# ======================

@router.put("/beds/update/{id}")
def update_bed(id: int, data: BedUpdate, db: Session = Depends(get_db)):

    bed = db.query(Bed).filter(Bed.id == id).first()

    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")

    bed.room_id = data.room_id
    bed.bed_number = data.bed_number
    bed.status = data.status

    db.commit()
    db.refresh(bed)

    return {
        "message": "Bed updated successfully",
        "data": bed
    }


# ======================
# DELETE BED
# ======================

@router.delete("/beds/{id}")
def delete_bed(id: int, db: Session = Depends(get_db)):

    bed = db.query(Bed).filter(Bed.id == id).first()

    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")

    db.delete(bed)
    db.commit()

    return {"message": "Bed deleted successfully"}
