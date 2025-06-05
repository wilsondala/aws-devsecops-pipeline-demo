# Usa uma imagem base Python leve
FROM python:3.10-slim

# Cria um usuário não-root chamado 'appuser' e seu diretório home
RUN useradd -m appuser

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo da aplicação
COPY app.py .

# Muda para o usuário não-root
USER appuser

# Exposição da porta da aplicação
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
