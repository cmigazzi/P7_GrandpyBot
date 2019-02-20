import pytest

from grandpy.parser.validator import QuestionValidator
from grandpy.parser.exceptions import InvalidQuestionException, NoSpacesException


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
