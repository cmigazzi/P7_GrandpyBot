import pytest

from grandpy.parser.validator import QuestionValidator
from grandpy.parser.exceptions import (InvalidQuestionException,
                                       NoSpacesException,
                                       NotGeographicException,
                                       NotEnoughWordsException)


def test_class():
    question = "Ou se trouve le stade de France ?"
    qv = QuestionValidator(question)
    assert qv


def test_interrogation_mark(questions):
    for question in questions.values():
        p = QuestionValidator(question["question"])
        assert p.interrogation_mark() is None
    with pytest.raises(InvalidQuestionException):
        QuestionValidator("Tu connais le musée d'Orsay").interrogation_mark()
    p_2 = QuestionValidator("Tu connais le musée d'Orsay ? ")
    assert p_2.interrogation_mark() is None


def test_spaces(questions):
    for question in questions.values():
        p = QuestionValidator(question["question"])
        assert p.spaces() is None
    with pytest.raises(NoSpacesException):
        QuestionValidator("connaistulavie?").spaces()


def test_geographic(questions):
    p_0 = QuestionValidator(questions[3]["question"])
    p_1 = QuestionValidator(questions[7]["question"])
    assert p_0.geographic() is None
    assert p_1.geographic() is None
    
    with pytest.raises(NotGeographicException):
        QuestionValidator("Quand peux-tu venir ?").geographic()
    with pytest.raises(NotGeographicException):
        QuestionValidator("Comment vas-tu ?").geographic()
    with pytest.raises(NotGeographicException):
        QuestionValidator("Pourquoi les oiseaux volent ?").geographic()
    with pytest.raises(NotGeographicException):
        QuestionValidator("Combien de livres as-tu lu ?").geographic()


def test_count_words(questions):
    for question in questions.values():
        p = QuestionValidator(question["question"])
        assert p.count_words() is None
    with pytest.raises(NotEnoughWordsException):
        QuestionValidator("Ca va ?").count_words()
