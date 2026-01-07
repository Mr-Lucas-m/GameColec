def test_create_console_as_admin(api_client, admin_token):
    response = api_client.post(
        "/api/v1/consoles",
        headers={
            "Authorization": f"Bearer {admin_token}"
        },
        json={
            "name": "PlayStation 5",
            "company": "Sony"
        }
    )

    assert response.status_code in (200, 201)

    body = response.json()
    assert "data" in body
    assert body["data"]["name"] == "PlayStation 5"
    assert body["data"]["company"] == "Sony"


def test_create_console_as_user_forbidden(api_client, user_token):
    response = api_client.post(
        "/api/v1/consoles",
        headers={
            "Authorization": f"Bearer {user_token}"
        },
        json={
            "name": "Xbox Series X",
            "company": "Microsoft"
        }
    )

    assert response.status_code == 403


def test_list_games_by_console(api_client, admin_token):
    console_response = api_client.post(
        "/api/v1/consoles",
        headers={
            "Authorization": f"Bearer {admin_token}"
        },
        json={
            "name": "Nintendo Switch",
            "company": "Nintendo"
        }
    )

    assert console_response.status_code in (200, 201)

    console_id = console_response.json()["data"]["id"]

    response = api_client.get(
        f"/api/v1/games/consoles/{console_id}",
        headers={
            "Authorization": f"Bearer {admin_token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)
