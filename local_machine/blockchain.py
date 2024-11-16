import hashlib
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

class Blockchain:
    def __init__(self):
        self.chain = []
        # Criação do bloco gênese
        self.create_block(previous_hash='0', log_data='Bloco Gênese')

    def create_block(self, log_data, previous_hash):
        # Função que cria um novo bloco na blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(time.time()),
            'log_data': log_data,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        return block

    def add_block(self, log_data):
        # Adiciona um novo bloco à blockchain usando os dados de log fornecidos
        previous_block = self.chain[-1]
        previous_hash = previous_block['hash']
        return self.create_block(log_data, previous_hash)

    def hash_block(self, block):
        # Função para gerar o hash do bloco
        block_string = f"{block['index']}{block['timestamp']}{block['log_data']}{block['previous_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def get_chain(self):
        # Função para retornar toda a blockchain
        return self.chain

# Classe para monitorar as mudanças no arquivo de log
class LogHandler(FileSystemEventHandler):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def on_modified(self, event):
        if event.src_path == "./local_logs.log":
            with open(event.src_path, 'r') as file:
                logs = file.readlines()
                # Adiciona o novo log à blockchain apenas se houver mudanças
                if logs:
                    new_log = logs[-1].strip()  # Pega apenas o último log
                    new_block = self.blockchain.add_block(new_log)
                    print(f"Logs adicionados à blockchain: {new_block}")

# Função principal que configura o logger e o monitoramento
def main():
    # Configurando o logger
    logging.basicConfig(filename='local_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Criando a blockchain
    blockchain = Blockchain()

    # Criando o observador para monitorar os logs
    event_handler = LogHandler(blockchain)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        # Aguarda eventos no sistema de arquivos
        while True:
            time.sleep(1)  # Mantém o script rodando para capturar eventos
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
