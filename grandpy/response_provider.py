
import random

from .responses import RESPONSES


class ResponseProvider():

    def __init__(self, exception=None):
        if exception is not None:
            self.exception = exception.name
        else:
            self.exception = None

    def provider(self):
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
        welcome = random.choice(RESPONSES["welcome"])
        self.response = welcome

    def no_interrogation_mark(self):
        no_interrogation_mark = random.choice(RESPONSES["interrogation_mark"])
        self.response = no_interrogation_mark

    def no_spaces(self):
        no_spaces = random.choice(RESPONSES["no_spaces"])
        self.response = no_spaces

    def not_geographic(self):
        not_geographic = random.choice(RESPONSES["not_geographic"])
        self.response = not_geographic

    def zero_result(self):
        zero_result = random.choice(RESPONSES["zero_result"])
        self.response = zero_result
