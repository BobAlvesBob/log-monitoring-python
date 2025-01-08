import hashlib
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Importa a função que envia logs ao servidor
from send_logs import send_logs

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

class BlockchainLogHandler(logging.Handler):
    def __init__(self, blockchain):
        super().__init__()
        self.blockchain = blockchain

    def emit(self, record):
        log_entry = self.format(record)
        # Adiciona um novo bloco à blockchain local
        new_block = self.blockchain.add_block(log_entry)
        print(f"Bloco adicionado localmente: {new_block}")

        # Envia o mesmo log ao servidor
        # Utiliza o "previous_hash" do bloco que acabamos de criar
        previous_hash = new_block["previous_hash"]
        send_logs(log_entry, previous_hash)

# Função principal que configura o logger e o monitoramento
def main():
    # Criando a blockchain local
    blockchain = Blockchain()

    # Criando o manipulador de logs que envia logs para a blockchain local
    # e depois faz o POST ao servidor
    blockchain_handler = BlockchainLogHandler(blockchain)
    blockchain_handler.setLevel(logging.INFO)
    blockchain_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

    # Configurando o logger
    logger = logging.getLogger('BlockchainLogger')
    logger.setLevel(logging.INFO)
    logger.addHandler(blockchain_handler)

    # Simulando eventos de log no terminal
    try:
        print("Monitorando os logs do terminal e adicionando-os à blockchain local e ao servidor...")
        while True:
            log_message = input("Digite uma mensagem de log (ou 'sair' para terminar): ")
            if log_message.lower() == 'sair':
                break
            logger.info(log_message)
    except KeyboardInterrupt:
        print("\nEncerrando o monitoramento.")

if __name__ == "__main__":
    main()
