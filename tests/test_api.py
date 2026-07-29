from uuid import uuid4

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def create_user_fixture():
    response = client.post(
        "/users",
        json={
            "name": "Usuario Teste",
            "email": f"teste_{uuid4().hex[:8]}@controltask.com",
            "password": "123456"
        }
    )
    assert response.status_code == 201
    return response.json()


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Joao Teste",
            "email": "joao@teste.com",
            "password": "123456"
        }
    )

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_task():
    user = create_user_fixture()

    response = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Teste Pytest",
            "description": "Executando teste automatizado",
            "priority": "HIGH"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Teste Pytest"


def test_list_tasks():
    user = create_user_fixture()

    # cria uma tarefa primeiro
    client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Task 1",
            "description": "Lista",
            "priority": "LOW"
        }
    )

    response = client.get(f"/users/{user['id']}/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_tasks_for_unknown_user_returns_404():
    response = client.get("/users/999999/tasks")

    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado."


def test_update_task():
    user = create_user_fixture()

    task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Original",
            "description": "Antes",
            "priority": "LOW"
        }
    ).json()

    task_id = task["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Atualizado",
            "description": "Depois",
            "priority": "MEDIUM",
            "status": "COMPLETED"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Atualizado"
    assert response.json()["status"] == "COMPLETED"


def test_delete_task():
    user = create_user_fixture()

    task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Delete me",
            "description": "Para deletar",
            "priority": "LOW"
        }
    ).json()

    task_id = task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
