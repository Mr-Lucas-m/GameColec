import sys
import os

# Garante que o Python encontre o pacote "app"
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture(scope="session")
def api_client():
    return client


def create_user(email: str, password: str, role: str):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": password,
            "role": role
        }
    )

    # 400 se o usuário já existir
    assert response.status_code in (200, 201, 400)
    return response.json() if response.status_code in (200, 201) else None


def login(email: str, password: str) -> str:
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert response.status_code == 200
    return response.json()["data"]["access_token"]


@pytest.fixture(scope="session")
def admin_token():
    create_user("admin@test.com", "123456", "admin")
    return login("admin@test.com", "123456")


@pytest.fixture(scope="session")
def user_token():
    create_user("user@test.com", "123456", "user")
    return login("user@test.com", "123456")
