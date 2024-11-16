import json
from blockchain import Blockchain

def verify_logs():
    with open('received_logs.json', 'r') as file:
        data = json.load(file)

    blockchain = Blockchain()
    for block_data in data[1:]:
        blockchain.add_block(block_data["data"])
    
    if blockchain.is_chain_valid():
        print("Blockchain dos logs é válida.")
    else:
        print("Inconsistências encontradas nos logs.")

if __name__ == "__main__":
    verify_logs()
