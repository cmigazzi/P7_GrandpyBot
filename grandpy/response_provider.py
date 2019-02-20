
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
        elif self.exception == None:
            self.welcome()
        return self.response

    def welcome(self):
        welcome = random.choice(RESPONSES["welcome"])
        self.response = welcome

    def no_interrogation_mark(self):
        no_interrogation_mark = random.choice(RESPONSES["interrogation_mark"])
        self.response = no_interrogation_mark

