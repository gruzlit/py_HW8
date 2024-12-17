import requests


base_url = "https://ru.yougile.com/api-v2"


def test_get_token():
    creds = {
        'login': 'avnspas@tutanota.com',
        'password': 'Abf4122_',
        'companyId': 'd6de3a64-9e7a-43b3-a600-9b8ba6073586'
    }
    resp = requests.post(base_url+'/auth/keys', json=creds)
    assert resp.status_code == 201

