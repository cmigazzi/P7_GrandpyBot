import re

from .exceptions import (InvalidQuestionException, NoSpacesException,
                         NotGeographicException,
                         NotEnoughWordsException)


class QuestionValidator():

    def __init__(self, question):
        self.question = question.lower().rstrip()

    def interrogation_mark(self):
        if not re.match(r"^.*\?$", self.question):
            raise InvalidQuestionException

    def spaces(self):
        if not re.search(r"\s", self.question):
            raise NoSpacesException

    def geographic(self):
        if re.search(r"(quand|comment|qui|pourquoi|combien)\s", self.question):
            raise NotGeographicException

    def count_words(self):
        if len(re.findall(r"(\s|-|')", self.question)) < 4:
            raise NotEnoughWordsException
