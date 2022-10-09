def test_request_example(client):
    response = client.get("/")
    assert response.data.decode('utf-8') == 'Hello, World!'
    # assert b"Hello, World!" in response.data