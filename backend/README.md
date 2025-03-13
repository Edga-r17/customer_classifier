# Backend - API de Clasificación de Clientes (FastAPI)

Este backend es un **microservicio** construido en **FastAPI** que clasifica a un cliente en un color basado en su **salario y gastos**.

## 🚀 Instalación y Ejecución


### 1️⃣ Crear entorno virtual e instalar dependencias

Usaremos `virtualenv` para crear un entorno virtual aislado para las dependencias del proyecto:
Crear el ambiente virtual usando [pyenv](https://github.com/pyenv/pyenv#installation)
Activar el ambiente virtual
```bash
pyenv activate <nombre_del_ambiente_creado>
```

Instala las dependencias requeridas desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt

```

### 2️⃣ Ejecutar el servidor FastAPI

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

El backend estará corriendo en:
🔗 http://127.0.0.1:8001

Puedes probar la API con Swagger UI:
🔗 http://127.0.0.1:8001/docs

### 3️⃣ Pruebas unitarias

```bash
pytest app/tests/test_main.py
```

## 🚀 Endpoints Disponibles en la API

| Método | Endpoint | Descripción |
|--------|---------|-------------|
| **POST** | `/api/classify/` | Recibe salario y gastos, devuelve el color del cliente|

Ejemplo de petición JSON:
```json
{
  "salary": 8000,
  "expenses": 2000
}
```
Respuesta esperada:
```json
{
  "color": "Verde"
}
```