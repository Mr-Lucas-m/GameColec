def test_create_game_as_admin(api_client, admin_token):
    # cria console
    console_response = api_client.post(
        "/api/v1/consoles",
        headers={
            "Authorization": f"Bearer {admin_token}"
        },
        json={
            "name": "PS4",
            "company": "Sony"
        }
    )

    assert console_response.status_code in (200, 201)

    console_id = console_response.json()["data"]["id"]

    # cria game
    response = api_client.post(
        "/api/v1/games",
        headers={
            "Authorization": f"Bearer {admin_token}"
        },
        json={
            "name": "God of War",
            "console_id": console_id
        }
    )

    assert response.status_code in (200, 201)
    assert response.json()["data"]["name"] == "God of War"


def test_create_game_as_user_forbidden(api_client, user_token):
    response = api_client.post(
        "/api/v1/games",
        headers={
            "Authorization": f"Bearer {user_token}"
        },
        json={
            "name": "Forbidden Game",
            "console_id": "00000000-0000-0000-0000-000000000000"
        }
    )

    assert response.status_code == 403
