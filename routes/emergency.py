from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Literal

router = APIRouter(tags=["Emergency"])

class EmergencyRequest(BaseModel):
    name: str
    age: int = Field(..., ge=0, le=120)
    gender: Literal["male", "female"]
    situation: Literal["critical", "normal"]

@router.post("/emergency/")
def create_emergency(request: EmergencyRequest):

    if request.situation == "critical":
        priority = "HIGH"
    else:
        priority = "NORMAL"

    return {
        "message": "Emergency request created successfully",
        "patient": request,
        "priority": priority
    }