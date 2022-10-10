def test_request_example(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data