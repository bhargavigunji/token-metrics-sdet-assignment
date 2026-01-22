def test_deposit_success(api_client, mock_blockchain):
    res = api_client.post("/deposit", json={"user": "0xabc", "amount": 50})
    assert res.status_code == 200

    body = res.json()
    assert body["status"] == "ok"
    assert body["tx_hash"] == "0xdeadbeef"



def test_deposit_rejects_zero(api_client):
    res = api_client.post("/deposit", json={"user": "0xabc", "amount": 0})
    assert res.status_code == 400
    assert res.json()["detail"] == "amount must be > 0"



def test_deposit_rpc_down(api_client, mock_blockchain):
    mock_blockchain.reset()
    mock_blockchain.add(
        mock_blockchain.POST,
        "https://fake-rpc.local",
        status=500,
        json={"error": "rpc down"},
    )

    res = api_client.post("/deposit", json={"user": "0xabc", "amount": 10})
    assert res.status_code == 502
    assert res.json()["detail"] == "blockchain unavailable"

