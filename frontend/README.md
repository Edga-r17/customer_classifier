# Frontend - Interfaz para Clasificación de Clientes (Django)

Este frontend está construido con **Django** y proporciona una interfaz web para que los usuarios ingresen su **salario y gastos**, y reciban la clasificación de color.

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

### 2️⃣ Configurar el backend en views.py

Si el backend está corriendo en otro servidor, cambia la variable FASTAPI_URL en `client_classifier/views.py`:

```bash
FASTAPI_URL = "http://127.0.0.1:8001/api/classify/"
```

### 3️⃣ Ejecutar el servidor Django

```bash
python manage.py runserver
```
