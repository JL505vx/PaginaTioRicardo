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

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Comando de arranque (produccion/demo en Render)
CMD ["/app/entrypoint.sh"]
