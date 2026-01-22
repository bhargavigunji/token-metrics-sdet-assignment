from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.rpc_client import RpcClient
from app.storage import InMemoryDB

app = FastAPI(title="Token Metrics Test API")

class DepositRequest(BaseModel):
    user: str
    amount: int

@app.on_event("startup")
def startup():
    app.state.db = InMemoryDB()
    app.state.db.seed()
    app.state.rpc_client = RpcClient(rpc_url="https://example-rpc.local")

@app.post("/deposit")
def deposit(req: DepositRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="amount must be > 0")

    
    try:
        tx_hash = app.state.rpc_client.send_deposit_tx(req.user, req.amount)
    except Exception:
        raise HTTPException(status_code=502, detail="blockchain unavailable")

    app.state.db.add_deposit(user=req.user, amount=req.amount, tx_hash=tx_hash)

    return {"status": "ok", "tx_hash": tx_hash}
