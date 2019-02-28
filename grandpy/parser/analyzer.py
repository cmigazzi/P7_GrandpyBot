"""Contains analyzer for the question send."""

import re

from .question_type import QuestionType
from .words_base import PRONOUNS, W_WORDS, STOP_WORDS


class QuestionAnalyzer():
    """Represent the analyze engine.

    Methods:
        set_words() -- Split words.
        get_words() --

    Constructor arguments:
        question {str} -- question to analyze

    """

    def __init__(self, question):
        """Please check help(QuestionAnalyzer) for more details."""
        self.question = question.lower().rstrip()
        self._words = self.set_words()
        self._type = self.set_type()
        self._pronoun = self.set_pronoun()

    def set_words(self):
        """Split words.

        Returns:
            [list] -- words

        """
        if re.search(r"(\.|!)", self.question):
            questions = re.split(r"(\.|!)", self.question)
            self.question = questions[-1]
        words = list(filter(None, re.split(r"\W+", self.question)))
        return words

    def get_words(self):
        """Return the words."""
        return self._words

    def set_type(self):
        """Define the type of the question.

        Returns:
            [Enum] -- QuestionType

        """
        words = self.get_words()
        if re.search(r"est(-|\s)ce que", self.question):
            q_type = QuestionType.STANDARD
        elif words[0] in PRONOUNS:
            q_type = QuestionType.COLLOQUIAL
        elif words[1] in PRONOUNS:
            q_type = QuestionType.FORMAL
        elif words[0] in W_WORDS or [w for w in words[:-2]
                                     if re.match(r"o(u|ù)", w)]:
            q_type = QuestionType.W_WORD
        else:
            q_type = QuestionType.KEYWORDS_FIRST
        return q_type

    def get_type(self):
        """Return the type of the question."""
        return self._type

    def set_pronoun(self):
        """Define the pronoun of the question.

        Returns:
            [str] -- pronoun

        """
        words = self.get_words()
        for word in words:
            if word in PRONOUNS:
                pronoun = word
                break
            else:
                pronoun = None

        return pronoun

    def get_pronoun(self):
        """Return the pronoun of the question."""
        return self._pronoun

    def get_keywords(self):
        """Select the keywords of the question.

        Returns:
            [list] -- selected keywords

        """
        q_type = self.get_type()
        words = self.get_words()

        if "adresse" in words:
            adress_id = words.index("adresse")
            target_keywords = words[adress_id+1:]

        elif q_type == QuestionType.W_WORD:
            target_keywords = words[3:]
        elif q_type == QuestionType.KEYWORDS_FIRST:
            target_keywords = words[:5]
        elif q_type == QuestionType.FORMAL:
            for word in words[:-2]:
                if word in W_WORDS and words.index(word):
                    w_word_id = words.index(word)
                    target_keywords = words[w_word_id+3:]
                    break
        else:
            target_keywords = words[5:]

        keywords = [w for w in target_keywords
                    if len(w) > 1 and w not in STOP_WORDS]

        return keywords
