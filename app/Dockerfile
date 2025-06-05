# Imagem base leve do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação, incluindo templates
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Define o comando padrão
CMD ["python", "app.py"]
