"""Contains the validator of question."""

import re

from .exceptions import (InvalidQuestionException, NoSpacesException,
                         NotGeographicException,
                         NotEnoughWordsException)


class QuestionValidator():
    """Represent the validator of question.

    It checks if a question is valid. If not, it raises exceptions.

    Raises:
        InvalidQuestionException -- Question is not valid.
        NoSpacesException -- No space in question.
        NotGeographicException -- Not Geographic.
        NotEnoughWordsException -- Not enough words in question.

    """

    def __init__(self, question):
        """Construct the QuestionValidator instance.

        Arguments:
            question {str} -- a question
        """
        self.question = question.lower().rstrip()

    def interrogation_mark(self):
        """Check if interrogation marl is present at the end."""
        if not re.match(r"^.*\?$", self.question):
            raise InvalidQuestionException

    def spaces(self):
        """Check if there is spaces between words."""
        if not re.search(r"\s", self.question):
            raise NoSpacesException

    def geographic(self):
        """Check if the question ask for a place."""
        if re.search(r"(quand|comment|qui|pourquoi|combien)\s", self.question):
            raise NotGeographicException

    def count_words(self):
        """Count words."""
        if len(re.findall(r"(\s|-|')", self.question)) < 4:
            raise NotEnoughWordsException
