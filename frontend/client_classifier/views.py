import requests
from django.shortcuts import render
from django.http import JsonResponse

FASTAPI_URL = "http://127.0.0.1:8001/api/classify/"

# Diccionario de colores de Bootstrap
BOOTSTRAP_COLORS = {
    "Azul": "primary",
    "Verde": "success",
    "Amarillo": "warning",
    "Rojo": "danger",
}

def classify_client(request):
    """Vista para recibir salario y gasto, y enviar la solicitud a FastAPI"""
    if request.method == "POST":
        salary = float(request.POST.get("salary", 0))
        expenses = float(request.POST.get("expenses", 0))

        response = requests.post(FASTAPI_URL, json={"salary": salary, "expenses": expenses})
        data = response.json()

        color = data.get("color", "Error")
        bootstrap_color = BOOTSTRAP_COLORS.get(color, "secondary")  

        return render(request, "result.html", {"color": bootstrap_color, "text_color": color})

    return render(request, "form.html")
