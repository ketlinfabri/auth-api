FROM python:3.10-slim

# Variáveis de ambiente para não gerar .pyc e forçar UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta da API
EXPOSE 8080

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
