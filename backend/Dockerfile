# ---- Fase 1: Build ----
# Compila las dependencias
FROM python:3.12-slim as builder

WORKDIR /app
COPY requirements.txt .
COPY requirements-dev.txt .

# 1. Instala TODAS las dependencias (dev + prod) para la etapa de pruebas y linter
RUN pip install --no-cache-dir -r requirements-dev.txt

# 2. Crea los wheels SOLO de las dependencias de producción para la imagen final
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

COPY ./app ./app

# ---- Fase 2: Final ----
# Construye la imagen final de producción
FROM python:3.12-slim

# Crear un usuario y grupo no root
RUN groupadd -r appuser && useradd --no-create-home -r -g appuser appuser

WORKDIR /app

# Copiamos las dependencias y el código
COPY --from=builder /app/wheels /wheels
COPY ./app .

# Como ROOT, instalamos todo en el sistema
RUN pip install --no-cache-dir /wheels/*

# Cambiar al usuario no root
USER appuser

# Exponemos el puerto
EXPOSE 8080

# HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD python -c "import sys, http.client; conn = http.client.HTTPConnection('localhost', 8080); conn.request('GET', '/health'); sys.exit(0) if conn.getresponse().status == 200 else sys.exit(1)"

# Ejecutamos Gunicorn como un módulo de Python para evitar problemas de PATH
ENTRYPOINT ["python", "-m", "gunicorn"]
CMD ["-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080", "main:app"]
