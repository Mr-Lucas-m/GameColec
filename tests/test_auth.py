def test_login_success(admin_token):
    assert admin_token is not None
    assert isinstance(admin_token, str)


def test_login_invalid_password(api_client):
    response = api_client.post(
        "/api/v1/auth/login",
        data={
            "username": "admin@test.com",
            "password": "senha_errada"
        }
    )

    assert response.status_code == 401
