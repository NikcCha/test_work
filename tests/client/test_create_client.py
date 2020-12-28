from methods.client import create_client


def test_create_client():
    response = create_client()
    if response.status_code == 400:
        assert response.json()['message'] == f'Cliet with this phone already exist in DataBase'
    else:
        assert response.status_code == 200
        assert response.json()['client_id'].type == int
