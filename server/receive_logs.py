from flask import Flask, request, jsonify
import json
import hashlib
import time

app = Flask(__name__)

# Blockchain do servidor
blockchain = []

def hash_block(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

@app.route('/receive_logs', methods=['POST'])
def receive_logs():
    new_block_data = request.get_json()

    # Verifica se todos os campos necessários estão presentes
    if 'log_data' not in new_block_data or 'previous_hash' not in new_block_data:
        return jsonify({"error": "Dados ausentes. 'log_data' e 'previous_hash' são necessários."}), 400

    # Verificar a integridade dos hashes
    if blockchain:
        last_block = blockchain[-1]
        if last_block['hash'] != new_block_data['previous_hash']:
            return jsonify({"error": "Hash do bloco anterior não corresponde. Verificação falhou."}), 400

    # Criar um novo bloco na blockchain do servidor
    block = {
        'index': len(blockchain) + 1,
        'timestamp': time.time(),
        'log_data': new_block_data['log_data'],
        'previous_hash': new_block_data['previous_hash'],
    }
    block['hash'] = hash_block(block)
    
    # Adiciona o novo bloco à blockchain do servidor
    blockchain.append(block)

    # Salva a blockchain em um arquivo (opcional)
    with open('received_blockchain.json', 'w') as file:
        json.dump(blockchain, file, indent=4)

    return jsonify({"message": "Logs recebidos e registrados na blockchain do servidor."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
