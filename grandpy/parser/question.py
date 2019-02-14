import re


class QuestionAnalyzer():

    def __init__(self, question):
        self.question = question.lower().rstrip()

    def is_question(self):
        if self.question[-1] == "?":
            return True
        else:
            return False

    def get_words(self):
        words = list(filter(None, re.split("\W+", self.question)))
        self.words = words
