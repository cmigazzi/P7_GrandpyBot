
import random

from .responses import RESPONSES


class ResponseProvider():

    def welcome(self):
        welcome = random.choice(RESPONSES["welcome"])
        return welcome
    
    def misunderstood(self):
        misunderstood = random.choice(RESPONSES["misunderstood"])
        return misunderstood

    def understood(self):
        understood = random.choice(RESPONSES["understood"])
        return understood
