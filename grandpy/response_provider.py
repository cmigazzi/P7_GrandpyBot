"""Contains the response provider for grandpy."""

import random

from .responses import RESPONSES


class ResponseProvider():
    """Represent the provider of responses.

    It selects appropriate response to the user question.

    Methods:
        provider() -- Provide repsonse function of the exception.
        welcome() -- Presentation answer.
        no_interrogation_mark() -- Select response when no interrogation mark.
        no_spaces() -- Select response when no spaces.
        not_geographic() -- Select response when not geographic.
        zero_result() -- Select resposne when no result.

    """

    def __init__(self, exception=None):
        """Construct ResponseProvider instance.

        Keyword Arguments:
            exception {str} -- Exception name (default: {None})

        """
        if exception is not None:
            self.exception = exception.name
        else:
            self.exception = None

    def provider(self):
        """Provide repsonse function of the exception."""
        if self.exception == "Invalid Question":
            self.no_interrogation_mark()
        elif self.exception == "No spaces":
            self.no_spaces()
        elif self.exception == "Not geographic":
            self.not_geographic()
        elif self.exception == "Zero result":
            self.zero_result()
        elif self.exception is None:
            self.welcome()
        return self.response

    def welcome(self):
        """Presentation answer."""
        welcome = random.choice(RESPONSES["welcome"])
        self.response = welcome

    def no_interrogation_mark(self):
        """Select response when no interrogation mark."""
        no_interrogation_mark = random.choice(RESPONSES["interrogation_mark"])
        self.response = no_interrogation_mark

    def no_spaces(self):
        """Select response when no spaces."""
        no_spaces = random.choice(RESPONSES["no_spaces"])
        self.response = no_spaces

    def not_geographic(self):
        """Select response when not geographic."""
        not_geographic = random.choice(RESPONSES["not_geographic"])
        self.response = not_geographic

    def zero_result(self):
        """Select resposne when no result."""
        zero_result = random.choice(RESPONSES["zero_result"])
        self.response = zero_result
