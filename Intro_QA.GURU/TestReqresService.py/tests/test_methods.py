from http import HTTPStatus

import pytest
import requests
from data import users, create_user, update_user, non_exist_id


@pytest.mark.parametrize('user_id', [5, 7])
def test_get_user(base_endpoint, user_id):
    response = requests.get(url=f"{base_endpoint[0]}/{users[user_id]['id']}")

    assert response.status_code == HTTPStatus.OK, f"Expected status code 200, but got {response.status_code}"
    assert response.json()['data']['id'] == users[user_id]['id']


def test_get_not_existing_user(base_endpoint):
    response = requests.get(url=f"{base_endpoint[0]}/{non_exist_id}")

    assert response.status_code == 404
    assert response.json() == {}


def test_create_user(base_endpoint):
    response = requests.post(url=base_endpoint[0], json=create_user)

    assert response.status_code == 201
    assert response.json()["name"] == create_user["name"]
    assert response.json()["job"] == create_user["job"]


def test_update_user(base_endpoint):
    response = requests.put(url=f"{base_endpoint[0]}/5", json=update_user)

    assert response.status_code == HTTPStatus.OK, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["name"] == update_user["name"]
    assert response.json()["job"] == update_user["job"]


def test_delete_user(base_endpoint):
    response = requests.delete(url=f"{base_endpoint[0]}/2")

    assert response.status_code == 204
