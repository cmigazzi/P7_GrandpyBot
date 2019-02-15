import re

from .question_type import QuestionType
from .words_base import PRONOUNS, W_WORDS, STOP_WORDS


class QuestionAnalyzer():

    def __init__(self, question):
        self.question = question.lower().rstrip()
        self._words = self.set_words()
        self._type = self.set_type()
        self._pronoun = self.set_pronoun()

    def set_words(self):
        words = list(filter(None, re.split("\W+", self.question)))
        return words

    def get_words(self):
        return self._words

    def set_type(self):
        words = self.get_words()
        if ["est", "ce", "que"] == words[0:3]:
            q_type = QuestionType.STANDARD
        elif words[0] in W_WORDS:
            q_type = QuestionType.W_WORD
        elif words[0] in PRONOUNS:
            q_type = QuestionType.COLLOQUIAL
        elif words[1] in PRONOUNS:
            q_type = QuestionType.FORMAL
        else:
            q_type = QuestionType.KEYWORDS_FIRST
        return q_type

    def get_type(self):
        return self._type

    def set_pronoun(self):
        words = self.get_words()
        for word in words:
            if word in PRONOUNS:
                pronoun = word
                break
            else:
                pronoun = None

        return pronoun

    def get_pronoun(self):
        return self._pronoun

    def is_question(self):
        if self.question[-1] == "?":
            return True
        else:
            return False

    def get_keywords(self):
        q_type = self.get_type()
        words = self.get_words()

        if "adresse" in words:
            adress_id = words.index("adresse")
            target_keywords = words[adress_id+1:]

        elif q_type == QuestionType.W_WORD:
            target_keywords = words[3:]
        elif q_type == QuestionType.KEYWORDS_FIRST:
            target_keywords = words[:5]
        elif (q_type == QuestionType.FORMAL
                and re.match(words[0], "^p[eo]u\w{0-2}[xtz]$")):
            target_keywords = words[6:]
        else:
            target_keywords = words[5:]

        keywords = [w for w in target_keywords
                    if len(w) > 1 and w not in STOP_WORDS]

        return keywords
