

def test_index(client):
    response = client.get('/')
    assert b"<title>GrandPy Bot</title>" in response.data
