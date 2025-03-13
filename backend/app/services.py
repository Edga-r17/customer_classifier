def classify_client(salary: float, expenses: float) -> str:
    """
    Clasifica a un cliente en un color basado en su saldo remanente
    (salario - gastos), siguiendo la lógica de negocio definida.

    Parámetros:
    - salary (float): Ingreso mensual del cliente.
    - expenses (float): Gastos mensuales del cliente.

    Retorna:
    - str: Un color que representa la situación financiera del cliente.
      - "Azul" si el remanente es mayor a 7000.
      - "Verde" si el remanente es mayor a 3000 y hasta 7000.
      - "Amarillo" si el remanente es mayor a 1000 y hasta 3000.
      - "Rojo" si el remanente es de 1000 o menor.
    """
    remaining = salary - expenses
    if remaining > 7000:
        return "Azul"
    elif remaining > 3000:
        return "Verde"
    elif remaining > 1000:
        return "Amarillo"
    else:
        return "Rojo"
