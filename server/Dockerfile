# Use uma imagem base do Python 3 (versão slim para ser mais leve)
FROM python:3-slim

# Exponha a porta 8000, que o Gunicorn usará
EXPOSE 8000

# Evita que o Python gere arquivos .pyc no contêiner
ENV PYTHONDONTWRITEBYTECODE=1

# Desativa o buffering para facilitar o log no contêiner
ENV PYTHONUNBUFFERED=1

# Instale as dependências listadas no requirements.txt
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os arquivos do projeto para o contêiner
COPY . /app

# Crie um usuário não-root para maior segurança e dê permissões sobre a pasta /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Execute o servidor usando o Gunicorn
# Altere o comando para referenciar o arquivo correto e a variável do app Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "receive_logs:app"]
