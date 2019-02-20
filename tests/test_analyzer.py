import pytest

from grandpy.parser.analyzer import QuestionAnalyzer
from grandpy.parser.question_type import QuestionType
from grandpy.parser.exceptions import InvalidQuestionException


def test_class(questions):
    for question in questions.values():
        p = QuestionAnalyzer(question["question"])
        assert p


def test_words(questions):
    for question in questions.values():
        p = QuestionAnalyzer(question["question"])
        p.set_words()
        assert p.get_words() == question["words"]


def test_type(questions):
    p0 = QuestionAnalyzer(questions[0]["question"])
    p1 = QuestionAnalyzer(questions[1]["question"])
    p2 = QuestionAnalyzer(questions[2]["question"])
    p3 = QuestionAnalyzer(questions[3]["question"])
    p4 = QuestionAnalyzer(questions[4]["question"])
    p5 = QuestionAnalyzer(questions[5]["question"])
    p6 = QuestionAnalyzer(questions[6]["question"])
    p7 = QuestionAnalyzer(questions[7]["question"])

    assert p0.get_type() == QuestionType.STANDARD
    assert p1.get_type() == QuestionType.FORMAL
    assert p2.get_type() == QuestionType.COLLOQUIAL
    assert p3.get_type() == QuestionType.W_WORD
    assert p4.get_type() == QuestionType.W_WORD
    assert p5.get_type() == QuestionType.KEYWORDS_FIRST
    assert p6.get_type() == QuestionType.FORMAL
    assert p7.get_type() == QuestionType.FORMAL


def test_set_pronoun(questions):
    p0 = QuestionAnalyzer(questions[0]["question"])
    p1 = QuestionAnalyzer(questions[1]["question"])
    p2 = QuestionAnalyzer(questions[2]["question"])
    p3 = QuestionAnalyzer(questions[3]["question"])
    p4 = QuestionAnalyzer(questions[4]["question"])
    p5 = QuestionAnalyzer(questions[5]["question"])
    p6 = QuestionAnalyzer(questions[6]["question"])
    p7 = QuestionAnalyzer(questions[7]["question"])

    assert p0.get_pronoun() == "tu"
    assert p1.get_pronoun() == "tu"
    assert p2.get_pronoun() == "tu"
    assert p3.get_pronoun() is None
    assert p4.get_pronoun() is None
    assert p5.get_pronoun() == "tu"
    assert p6.get_pronoun() == "vous"
    assert p7.get_pronoun() == "tu"


def test_get_keywords(questions):
    p0 = QuestionAnalyzer(questions[0]["question"])
    kw_0 = p0.get_keywords()
    assert kw_0 == questions[0]["keywords"]

    p1 = QuestionAnalyzer(questions[1]["question"])
    kw_1 = p1.get_keywords()
    assert kw_1 == questions[1]["keywords"]

    p2 = QuestionAnalyzer(questions[2]["question"])
    kw_2 = p2.get_keywords()
    assert kw_2 == questions[2]["keywords"]

    p3 = QuestionAnalyzer(questions[3]["question"])
    kw_3 = p3.get_keywords()
    assert kw_3 == questions[3]["keywords"]

    p4 = QuestionAnalyzer(questions[4]["question"])
    kw_4 = p4.get_keywords()
    assert kw_4 == questions[4]["keywords"]

    p5 = QuestionAnalyzer(questions[5]["question"])
    kw_5 = p5.get_keywords()
    assert kw_5 == questions[5]["keywords"]

    p6 = QuestionAnalyzer(questions[6]["question"])
    kw_6 = p6.get_keywords()
    assert kw_6 == questions[6]["keywords"]

    p7 = QuestionAnalyzer(questions[7]["question"])
    kw_7 = p7.get_keywords()
    assert kw_7 == questions[7]["keywords"]
