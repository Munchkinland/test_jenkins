# Usa la imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de la calculadora al contenedor
COPY calculadora.py .

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "calculadora.py"]
