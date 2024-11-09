import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        record = f'{self.index}{self.previous_hash}{self.data}{self.timestamp}'
        return hashlib.sha256(record.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Initialize the blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block(1, my_blockchain.get_latest_block().hash, "First Block"))
my_blockchain.add_block(Block(2, my_blockchain.get_latest_block().hash, "Second Block"))
my_blockchain.add_block(Block(3, my_blockchain.get_latest_block().hash, "Third Block"))

# Verify the blockchain’s validity
print("Blockchain valid:", my_blockchain.is_chain_valid())

# Display each block in the chain
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Current Hash: {block.hash}")
    print(f"Data: {block.data}")
    print(f"Timestamp: {block.timestamp}")
    print("-" * 30)


# How This Blockchain Works
# Genesis Block: The blockchain begins with a genesis block, a unique starting block without a previous hash.
# Adding Blocks: Each new block stores the hash of the previous block, creating a chain.
# Hashing: Each block calculates its hash based on its contents. If a block’s data changes, its hash changes, breaking the chain.
# Validation: We check the validity of the blockchain by verifying that each block’s hash matches its recalculated hash and that it correctly references the previous block’s hash.
# Next Steps and Improvements
# This basic blockchain lacks some features present in real-world blockchains, such as:

# Proof of Work (PoW): A mechanism to prevent spam and tampering by making it computationally difficult to add a block.
# Decentralization: In a real blockchain, multiple nodes contribute to the chain instead of just one.
# Transactions and Wallets: You could enhance this blockchain by adding wallet functionality, transaction handling, and digital signatures.
# By experimenting with these additional features, you can gain deeper insight into how blockchains work in practice. Let me know if you’d like help implementing any of these advanced concepts!