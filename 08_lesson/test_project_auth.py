import requests


base_url = "https://ru.yougile.com/api-v2"

def test_auth():
    creds = {
        'login': 'avnspas@tutanota.com',
        'password': 'Abf4122_'
        }
    resp = requests.post(base_url+'/auth/companies', json=creds)
    assert resp.status_code == 200





