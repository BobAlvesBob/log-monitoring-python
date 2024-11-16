import os
import requests

def send_logs():
    server_url = os.getenv("SERVER_URL", "http://server:8000")  
    data = {"log_data": "Conteúdo do log aqui", "previous_hash": "0"}  # Exemplo de conteúdo de log
    response = requests.post(f"{server_url}/receive_logs", json=data)
    print(response.status_code)

if __name__ == "__main__":
    send_logs()
