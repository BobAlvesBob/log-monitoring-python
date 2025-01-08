import os
import requests

def send_logs(log_message, previous_hash):
    server_url = os.getenv("SERVER_URL", "http://server:8000")
    data = {
        "log_data": log_message,
        "previous_hash": previous_hash
    }
    response = requests.post(f"{server_url}/receive_logs", json=data)
    print("Resposta do servidor:", response.text, response.status_code)

if __name__ == "__main__":
    # Exemplo de teste
    send_logs("Log de teste local", "0")
