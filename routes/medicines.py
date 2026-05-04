from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import Medicine
import crud

router = APIRouter()

@router.get("/medicines", response_model=list[Medicine])
def get_medicines(db: Session = Depends(get_db)):
    return crud.get_medicines(db)