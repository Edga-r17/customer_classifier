from fastapi import APIRouter
from app.models import ClientData
from app.services import classify_client

router = APIRouter()

@router.post("/api/classify/")
def classify(data: ClientData):
    color = classify_client(data.salary, data.expenses)
    return {"color": color}
