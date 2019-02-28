"""Contains tests suite for the route index."""

import json


def test_get(client):
    """Test GET method."""
    response = client.get('/')
    assert b"<title>GrandPy Bot</title>" in response.data


def test_post(client):
    """Test POST method."""
    json_data = json.dumps({"question": "Ou se trouve le stade de France ?"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": true" in response.data


def test_invalid_mark_post(client):
    """Test if no interrogation mark."""
    json_data = json.dumps({"question": "Ou se trouve le stade de France"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data


def test_no_spaces_post(client):
    """Test if no spaces in the question."""
    json_data = json.dumps({"question": "Ousetrouvelestade"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data


def test_not_geographic_post(client):
    """Test if question is not geographical."""
    json_data = json.dumps({"question": "Combien de livres as-tu lu ?"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data


def test_zero_result(client, zero_result_google_api_call):
    """Test if google maps API return zero result."""
    json_data = json.dumps({"question": "Ou se trouve lkjq ?"})
    response = client.post('/', data=json_data,
                           content_type="application/json")
    assert b"\"is_valid\": false, \"message\":" in response.data
