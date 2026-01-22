import pytest
import responses
from fastapi.testclient import TestClient

from app.main import app
from app.storage import InMemoryDB
from app.services.rpc_client import RpcClient

RPC_URL = "https://fake-rpc.local"

@pytest.fixture
def mock_blockchain():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.POST,
            RPC_URL,
            json={"result": "0xdeadbeef"},
            status=200,
        )
        yield rsps

@pytest.fixture
def seeded_db():
    db = InMemoryDB()
    db.seed()
    return db

@pytest.fixture
def api_client(seeded_db):
    app.state.db = seeded_db
    app.state.rpc_client = RpcClient(rpc_url=RPC_URL)
    return TestClient(app)
