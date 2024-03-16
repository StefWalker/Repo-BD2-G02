import requests
import pytest

@pytest.fixture(scope='module')
def jwt_token():
    # Realizar la solicitud POST para obtener el token JWT
    url = 'http://localhost:5002/api/user'
    payload = {"username": "Ahmed", "password": "$tr0ngP@55!"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201  # Asegurar que la solicitud fue exitosa
    token = response.json().get('access_token')
    assert token is not None  # Asegurar que se obtuvo un token
    return token

def test_tasks_get(jwt_token):
    # Usar el token JWT obtenido en la solicitud GET a /api/tasks
    url = 'http://localhost:5002/api/tasks'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_tasks_post(jwt_token):
    # Usar el token JWT obtenido en la solicitud POST a /api/tasks
    url = 'http://localhost:5002/api/tasks'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    task_data = {
        "name": "Jan",
        "description": "user",
        "due_date": "2028-05-09",
        "status": "complete",
        "usuario_id": 1
    }
    response = requests.post(url, json=task_data, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_tasks_put(jwt_token):
    # Usar el token JWT obtenido en la solicitud PUT a /api/tasks
    url = 'http://localhost:5002/api/tasks'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    task_data = {
        "name": "Jana",
        "description": "user",
        "due_date": "2028-05-09",
        "status": "complete",
        "usuario_id": 1,
        "id": 5
    }
    response = requests.put(url, json=task_data, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_tasks_delete(jwt_token):
    # Usar el token JWT obtenido en la solicitud DELETE a /api/tasks
    url = 'http://localhost:5002/api/tasks/5'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_user_get(jwt_token):
    # Usar el token JWT obtenido en la solicitud GET a /api/user
    url = 'http://localhost:5002/api/user'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_user_post(jwt_token):
    # Usar el token JWT obtenido en la solicitud POST a /api/user
    url = 'http://localhost:5002/api/user'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    user_data = {
        "username": "Jan",
        "password": "P@ssw0r123!"
    }
    response = requests.post(url, json=user_data, headers=headers)
    assert response.status_code == 201  # Asegurar que la solicitud fue exitosa

def test_user_put(jwt_token):
    # Usar el token JWT obtenido en la solicitud PUT a /api/user
    url = 'http://localhost:5002/api/user'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    user_data = {
        "name": "kennethh",
        "password": "fuhfbcw8yg",
        "user_id": 5
    }
    response = requests.put(url, json=user_data, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa

def test_user_delete(jwt_token):
    # Usar el token JWT obtenido en la solicitud DELETE a /api/user
    url = 'http://localhost:5002/api/user/5'
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200  # Asegurar que la solicitud fue exitosa
