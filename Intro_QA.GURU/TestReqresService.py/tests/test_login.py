
from http import HTTPStatus

import requests
from data import login_user


def test_login_successful(base_endpoint):
    response = requests.post(url=base_endpoint[2], json=login_user)

    assert response.status_code == HTTPStatus.OK, f"Expected status code 200, but got {response.status_code}"
    assert 'token' in response.json()


def test_login_non_email(base_endpoint):
    response = requests.post(url=base_endpoint[2], json={"password": login_user["password"]})

    assert response.status_code == 400
    assert 'error' in response.json()
    assert response.json()["error"] == "Missing email or username"


def test_login_non_password(base_endpoint):
    response = requests.post(url=base_endpoint[2], json={"email": login_user["email"]})

    assert response.status_code == 400
    assert 'error' in response.json()
    assert response.json()["error"] == "Missing password"
