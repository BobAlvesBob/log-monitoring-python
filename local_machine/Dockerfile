# Use uma imagem base de Python 3.8
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos da pasta local_machine para o contêiner
COPY . .

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Execute um script de entrada quando o contêiner iniciar
# Aqui você pode usar o entrypoint.sh para executar `logger.py` e depois `send_logs.py`
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Defina o ponto de entrada do contêiner
ENTRYPOINT ["/app/entrypoint.sh"]
