import requests

base_url = "https://ru.yougile.com/api-v2"

#позитивный тест
def test_create():
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }
    creds = {
        "title": "тест1",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
    }
    resp = requests.post(base_url + '/projects', json=creds, headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 201
#негативный тест(отсутствие ключа)
def test_create1():
    my_headers = {
        'Authorization': ''
    }
    creds = {
        "title": "тест1",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
    }
    resp = requests.post(base_url + '/projects', json=creds, headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 201
#негативный тест(отсутствие tytle)
def test_create2():
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }
    creds = {
        "title": "",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
    }
    resp = requests.post(base_url + '/projects', json=creds, headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 201