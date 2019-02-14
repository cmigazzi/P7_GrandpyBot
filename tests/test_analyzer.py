from grandpy.parser.analyzer import QuestionAnalyzer
from grandpy.parser.question_type import QuestionType


def test_class(questions):
    for question in questions.values():
        p = QuestionAnalyzer(question["question"])
        assert p


def test_is_question(questions):
    for question in questions.values():
        p = QuestionAnalyzer(question["question"])
        assert p.is_question() is True
    p_1 = QuestionAnalyzer("Tu connais le musée d'Orsay")
    p_2 = QuestionAnalyzer("Tu connais le musée d'Orsay ? ")
    assert p_1.is_question() is False
    assert p_2.is_question() is True


def test_get_words(questions):
    for question in questions.values():
        p = QuestionAnalyzer(question["question"])
        p.get_words()
        assert p.words == question["words"]


def test_get_type(questions):
    p0 = QuestionAnalyzer(questions[0]["question"])
    p1 = QuestionAnalyzer(questions[1]["question"])
    p2 = QuestionAnalyzer(questions[2]["question"])
    p3 = QuestionAnalyzer(questions[3]["question"])
    p4 = QuestionAnalyzer(questions[4]["question"])
    p5 = QuestionAnalyzer(questions[5]["question"])
    p0.get_type()
    p1.get_type()
    p2.get_type()
    p3.get_type()
    p4.get_type()
    p5.get_type()
    assert p0.type == QuestionType.STANDARD
    assert p1.type == QuestionType.FORMAL
    assert p2.type == QuestionType.COLLOQUIAL
    assert p3.type == QuestionType.W_WORD
    assert p4.type == QuestionType.W_WORD
    assert p5.type == QuestionType.KEYWORDS_FIRST


def test_get_pronoun(questions):
    p0 = QuestionAnalyzer(questions[0]["question"])
    p1 = QuestionAnalyzer(questions[1]["question"])
    p2 = QuestionAnalyzer(questions[2]["question"])
    p3 = QuestionAnalyzer(questions[3]["question"])
    p4 = QuestionAnalyzer(questions[4]["question"])
    p5 = QuestionAnalyzer(questions[5]["question"])
    p6 = QuestionAnalyzer(questions[6]["question"])
    p0.get_pronoun()
    p1.get_pronoun()
    p2.get_pronoun()
    p3.get_pronoun()
    p4.get_pronoun()
    p5.get_pronoun()
    p6.get_pronoun()
    assert p0.pronoun == "tu"
    assert p1.pronoun == "tu"
    assert p2.pronoun == "tu"
    assert p3.pronoun is None
    assert p4.pronoun is None
    assert p5.pronoun == "tu"
    assert p6.pronoun == "vous"
# def test_split(questions):
#     for question in questions.values():
#         assert Parser(question["question"]).words == question["words"]


# def test_clean(questions, base_stop):
#     for question in questions.values():
#         parser = Parser(question["question"])
#         words = parser.words
#         result = [w for w in words if w not in base_stop]
#         parser.clean()
#         assert parser.words == result


# def test_keywords(questions):
#     for question in questions.values():
#         parser = Parser(question["question"])
#         parser.clean()
#         parser.get_keywords()
#         assert parser.keywords == question["keywords"]
