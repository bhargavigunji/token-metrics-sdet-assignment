import requests

class RpcClient:
    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url

    def send_deposit_tx(self, user: str, amount: int) -> str:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tm_sendDeposit",
            "params": {"user": user, "amount": amount},
        }

        res = requests.post(self.rpc_url, json=payload, timeout=5)
        res.raise_for_status()
        data = res.json()

        return data.get("result", "0x0")
