import sys
import os
import pytest
from fastapi.testclient import TestClient

# garante import do app
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.main import app
from app.core.config import settings


@pytest.fixture(scope="session")
def api_client():
    """
    Garante que os eventos de startup sejam executados
    (criação do admin, init_db, etc)
    """
    with TestClient(app) as client:
        yield client


def login(client: TestClient, email: str, password: str) -> str:
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
def admin_token(api_client):
    """
    Admin é criado automaticamente no startup
    """
    return login(
        api_client,
        settings.ADMIN_EMAIL,
        settings.ADMIN_PASSWORD
    )


@pytest.fixture(scope="session")
def user_token(api_client, admin_token):
    """
    User comum criado pelo ADMIN
    """
    response = api_client.post(
        "/api/v1/auth/register",
        headers={
            "Authorization": f"Bearer {admin_token}"
        },
        json={
            "email": "user@test.com",
            "password": "123456",
            "role": "user"
        }
    )

    # 201 criado | 400 já existe
    assert response.status_code in (201, 400)

    return login(api_client, "user@test.com", "123456")
