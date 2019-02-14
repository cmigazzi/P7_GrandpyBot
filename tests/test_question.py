from grandpy.parser.question import QuestionAnalyzer


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
