# Imagen base
FROM python:3.12-slim

# Configuracion basica
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Codigo del proyecto
COPY . /app/

EXPOSE 8000

# Comando por defecto (desarrollo local)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
