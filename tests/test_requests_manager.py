"""Contains tests suite for RequestManager."""

import pytest

from grandpy.requests_manager import RequestsManager
from grandpy.parser.analyzer import QuestionAnalyzer
from grandpy.parser.exceptions import ZeroResultException


def test_class_exist():
    """Test if class exist."""
    rm = RequestsManager("Ou es le stade de france ?")
    assert rm


def test_analyze(questions, ):
    """Test constructor."""
    for question in questions.values():
        rm = RequestsManager(question["question"])
        assert isinstance(rm.question, QuestionAnalyzer)


def test_get_geocodes():
    """Test get_geocode() method."""
    question = "Ou se trouve le Stade de France ?"
    rm = RequestsManager(question)
    assert rm.get_geocode() == {'lat': 48.9244592, 'lng': 2.3601645}


def test_get_adress():
    """Test get_adress() method."""
    question = "Ou se trouve le Stade de France ?"
    rm = RequestsManager(question)
    assert rm.get_adress() == "Stade de France, 93200 Saint-Denis"


def test_wikimedia():
    """Test get_articles() method."""
    question = "Ou se trouve le Stade de France ?"
    rm = RequestsManager(question)
    assert rm.get_articles() == ['Stade de France',
                                 'Saint-Denis – Porte de Paris (Paris Métro)',
                                 'Lycée Suger',
                                 'La Plaine–Stade de France station']


def test_get_summary():
    """Test get_summary() method."""
    question = "Ou se trouve le Stade de France ?"
    rm = RequestsManager(question)
    assert rm.get_summary() == ("Le Stade de France est le plus grand "
                                "stade de football français avec 80 698 "
                                "places en configuration football/rugby. "
                                "Il se situe dans le quartier de la Plaine "
                                "Saint-Denis à Saint-Denis, dans la proche "
                                "banlieue nord de Paris.")


def test_gmaps_zero_results(zero_result_google_api_call):
    """Test when google maps API return zero result."""
    question = "Ou se trouve lkjq ?"
    with pytest.raises(ZeroResultException):
        RequestsManager(question)
