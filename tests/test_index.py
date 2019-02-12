import pytest

def test_index_return(client):
    response = client.get('/')
    print(response.data)
    assert b"Hello" in response.data
