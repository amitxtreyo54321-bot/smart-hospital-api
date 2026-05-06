from fastapi import APIRouter

router = APIRouter(tags=["Hospitals"])

# Get all hospitals
@router.get("/hospitals/")
def get_hospitals():
    return [
        {"id": 1, "name": "AIIMS Patna", "location": "Patna"},
        {"id": 2, "name": "IGIMS Patna", "location": "Patna"},
        {"id": 3, "name": "PMCH PATNA", "location": "Patna"},
        {"id": 4, "name": "PARAS PATNA", "location": "patna"},
        {"id": 5, "name": "MAHAVIR PATNA", "location": "patna"},
        {"id": 6, "name": "MIMS PATNA", "location": "patna"}
    ]


# Nearby hospitals
@router.get("/hospitals/nearby/")
def nearby_hospitals(lat: float, lng: float):
    return {
        "message": "Nearby hospitals in Patna",
        "user_location": {"lat": lat, "lng": lng},
        "hospitals": [
            {"name": "AIIMS Patna", "distance": "5 km", "emergency": True},
            {"name": "IGIMS Patna", "distance": "4 km", "emergency": True},
            {"name": "PMCH", "distance": "3 km", "emergency": True},
            {"name": "Paras HMRI Hospital", "distance": "6 km", "emergency": True},
            {"name": "Ruban Memorial Hospital", "distance": "2.5 km", "emergency": False},
            {"name": "Ford Hospital", "distance": "7 km", "emergency": True},
            {"name": "Kurji Holy Family Hospital", "distance": "3.5 km", "emergency": True}
        ]
    }


# Bed availability
@router.get("/beds/{hospital_id}")
def get_beds(hospital_id: int):

    data = {
        1: {
            "hospital_name": "PMCH",
            "icu_beds": 5,
            "general_beds": 20,
            "oxygen_beds": 10
        },
        2: {
            "hospital_name": "Paras HMRI Hospital",
            "icu_beds": 3,
            "general_beds": 15,
            "oxygen_beds": 8
        },
        3: {
            "hospital_name": "Ruban Memorial Hospital",
            "icu_beds": 2,
            "general_beds": 10,
            "oxygen_beds": 5
        },
        4: {
            "hospital_name": "Ford Hospital",
            "icu_beds": 6,
            "general_beds": 25,
            "oxygen_beds": 12
        },
        5: {
            "hospital_name": "Mediversal Hospital",
            "icu_beds": 7,
            "general_beds": 30,
            "oxygen_beds": 25
        },
        6: {"hospital_name": "Apollo Hospital",
            "icu_beds": 6,
            "general_beds": 19,
            "oxygen_beds": 15
        }
    }

    return data.get(hospital_id, {"error": "Hospital not found"})


# Emergency request
@router.post("/emergency/")
def create_emergency():
    return {"message": "Emergency request created successfully"}