class InMemoryDB:
    def __init__(self):
        self.deposits = []
        self.protocols = []

    def seed(self):
        self.protocols = [
            {"name": "protocolA", "chain": "testnet"},
            {"name": "protocolB", "chain": "testnet"},
        ]

    def add_deposit(self, user: str, amount: int, tx_hash: str):
        self.deposits.append({"user": user, "amount": amount, "tx_hash": tx_hash})
