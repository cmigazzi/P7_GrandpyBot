import json


def test_get(client):
    response = client.get('/')
    assert b"<title>GrandPy Bot</title>" in response.data


def test_post(client):
    json_data = json.dumps({"question": "Ou se trouve le stade de France ?"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": true" in response.data


def test_invalid_mark_post(client):
    json_data = json.dumps({"question": "Ou se trouve le stade de France"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data


def test_no_spaces_post(client):
    json_data = json.dumps({"question": "Ousetrouvelestade"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data


def test_not_geographic_post(client):
    json_data = json.dumps({"question": "Combien de livres as-tu lu ?"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data
   