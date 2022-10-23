from tests.consts import book_model_post_json


def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_book_model_get(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_book_model_post(client):
    response = client.post("/books", json=book_model_post_json)
    assert response.status_code == 200
    assert (
        f'Book with title: {book_model_post_json["title"]} and author {book_model_post_json["author"]} successfully added'
        in str(response.data)
    )
