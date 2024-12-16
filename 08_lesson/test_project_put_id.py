import requests

base_url = "https://ru.yougile.com/api-v2"

#позитивный тест
def test_put_id():
    my_body = {
        "deleted": True,
        "title": "тест1",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
            }

    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.put(base_url +'/projects/1900e404-767f-4426-b3c0-9baaa2c8f43f', json=my_body, headers=my_headers )
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


# негативный тест (вместо True - False) - Баг
def test_put_id1():
    my_body = {
        "deleted": False,
        "title": "тест1",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
            }

    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.put(base_url +'/projects/1900e404-767f-4426-b3c0-9baaa2c8f43f', json=my_body, headers=my_headers )
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


# негативный тест (отсутствует id)
def test_put_id2():
    my_body = {
        "deleted": False,
        "title": "тест1",
        "users": {"d4dbd97e-1072-42b8-9987-710b8c4e04d3": "admin"}
            }

    my_headers = {
        'Authorization': 'Bearer zWlDAGlP4Hn5KO9EFM1qj3Wijdchn5sS9t4+1YEye+c57TM-0lGv4miMyUnW1TDQ'
    }

    resp = requests.put(base_url +'/projects/', json=my_body, headers=my_headers )
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200