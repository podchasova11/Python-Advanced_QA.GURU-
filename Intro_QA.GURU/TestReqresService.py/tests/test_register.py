from http import HTTPStatus

import requests
from data import register_user


def test_register_successful(base_endpoint):
    response = requests.post(url=base_endpoint[1], json=register_user)

    assert response.status_code == HTTPStatus.OK, f"Expected status code 200, but got {response.status_code}"
    assert 'id' in response.json() and 'token' in response.json()


def test_register_non_password(base_endpoint):
    response = requests.post(url=base_endpoint[1], json={"email": register_user["email"]})

    assert response.status_code == 400
    assert 'error' in response.json()
    assert response.json()["error"] == "Missing password"


def test_register_non_email(base_endpoint):
    response = requests.post(url=base_endpoint[1], json={"password": register_user["password"]})

    assert response.status_code == 400
    assert 'error' in response.json()
    assert response.json()["error"] == "Missing email or username"
