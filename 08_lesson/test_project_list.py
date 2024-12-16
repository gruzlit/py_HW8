import requests


base_url = "https://ru.yougile.com/api-v2"
#позитивный тест
def test_projects_list():
    creds = {
        'login': 'avnspas@tutanota.com',
        'password': 'Abf4122_'
    }
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }
    resp = requests.get(base_url+'/projects', json=creds,  headers = my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200

#негативный тест(неверный статус код)
def test_projects_list1():
    creds = {
        'login': 'avnspas@tutanota.com',
        'password': 'Abf4122_'
    }
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }
    resp = requests.get(base_url+'/projects', json=creds,  headers = my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 201

#негативный тест(пустой пароль) - Баг
def test_projects_list2():
    creds = {
        'login': '',
        'password': ''
    }
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }
    resp = requests.get(base_url+'/projects', json=creds,  headers = my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200