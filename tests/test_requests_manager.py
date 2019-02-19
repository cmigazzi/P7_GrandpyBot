

from grandpy.requests_manager import RequestsManager
from grandpy.parser.analyzer import QuestionAnalyzer


def test_class_exist():
    rm = RequestsManager("Ou es tu ?")
    assert rm


def test_analyze(questions):
    for question in questions.values():
        rm = RequestsManager(question["question"])
        assert isinstance(rm.question, QuestionAnalyzer)


def test_get_geocodes(questions):
    question = questions[0]["question"]
    rm = RequestsManager(question)
    assert rm._geocode == {'lat': 48.9244592, 'lng': 2.3601645}


def test_wikimedia(questions):
    question = questions[0]["question"]
    rm = RequestsManager(question)
    assert rm._articles == ['Stade de France',
                            'Saint-Denis – Porte de Paris (Paris Métro)',
                            'Lycée Suger', 'La Plaine–Stade de France station']
