# Imagem base
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exposição da porta
EXPOSE 5000

# Comando de execução
CMD ["python", "app.py"]
