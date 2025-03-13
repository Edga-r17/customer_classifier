from fastapi import APIRouter
from app.models import ClientData
from app.services import classify_client

router = APIRouter()

@router.post("/api/classify/")
def classify(data: ClientData):
    """
    Recibe un objeto JSON con los datos del cliente (salario y gastos),
    calcula el color correspondiente según la lógica de negocio y 
    devuelve un diccionario con el color asignado.
    """
    color = classify_client(data.salary, data.expenses)
    return {"color": color}
