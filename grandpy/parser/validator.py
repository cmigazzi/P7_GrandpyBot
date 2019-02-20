import re

from .exceptions import InvalidQuestionException, NoSpacesException

class QuestionValidator():

    def __init__(self, question):
        self.question = question.lower().rstrip()

    def interrogation_mark(self):
        if not re.match(r"^.*\?$", self.question):
            raise InvalidQuestionException

    def spaces(self):
        if not re.search(r"\s", self.question):
            raise NoSpacesException
  
