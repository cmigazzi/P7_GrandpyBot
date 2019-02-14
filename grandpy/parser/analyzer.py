import re

from .question_type import QuestionType
from .words_base import PRONOUNS, W_WORDS


class QuestionAnalyzer():

    def __init__(self, question):
        self.question = question.lower().rstrip()
        self.words = None

    def is_question(self):
        if self.question[-1] == "?":
            return True
        else:
            return False

    def get_words(self):
        words = list(filter(None, re.split("\W+", self.question)))
        self.words = words

    def get_type(self):
        if not self.words:
            self.get_words()

        if ["est", "ce", "que"] == self.words[0:3]:
            self.type = QuestionType.STANDARD
        elif self.words[0] in W_WORDS:
            self.type = QuestionType.W_WORD
        elif self.words[0] in PRONOUNS:
            self.type = QuestionType.COLLOQUIAL
        elif self.words[1] in PRONOUNS:
            self.type = QuestionType.FORMAL
        else:
            self.type = QuestionType.KEYWORDS_FIRST

    def get_pronoun(self):
        if not self.words:
            self.get_words()

        for word in self.words:
            if word in PRONOUNS:
                self.pronoun = word
                break
            else:
                self.pronoun = None
