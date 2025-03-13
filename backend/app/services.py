def classify_client(salary: float, expenses: float) -> str:
    remaining = salary - expenses
    if remaining > 7000:
        return "Azul"
    elif remaining > 3000:
        return "Verde"
    elif remaining > 1000:
        return "Amarillo"
    else:
        return "Rojo"
