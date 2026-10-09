import requests


PORT = 5001
BASE_URL = f"http://127.0.0.1:{PORT}"


def test_home():
    response = requests.get(BASE_URL + "/")
    assert response.status_code == 999


def test_healthz():
    response = requests.get(BASE_URL + "/healthz")
    assert response.status_code == 200
    assert response.text == "OK"


def test_books():
    response = requests.get(BASE_URL + "/books")

    assert response.status_code == 200

    books = response.json()

    assert len(books) >= 3
    assert books[0]["title"] == "Абай жолы"


def test_book_by_id():
    response = requests.get(BASE_URL + "/books/1")

    assert response.status_code == 200

    book = response.json()

    assert book["title"] == "Абай жолы"


def test_book_not_found():
    response = requests.get(BASE_URL + "/books/999")

    assert response.status_code == 404
