import requests

base_url = "https://ru.yougile.com/api-v2"

#позитивный тест
def test_get_id():
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.get(base_url +'/projects/1900e404-767f-4426-b3c0-9baaa2c8f43f', headers=my_headers )
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200

#негативный тест (нет projects)
def test_get_id1():
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.get(base_url +'//1900e404-767f-4426-b3c0-9baaa2c8f43f', headers=my_headers )
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


# негативный тест (нет application/json)
def test_get_id2():
    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.get(base_url +'/projects/1900e404-767f-4426-b3c0-9baaa2c8f43f', headers=my_headers )
    assert resp.headers["Content-Type"] == '; charset=utf-8'
    assert resp.status_code == 200