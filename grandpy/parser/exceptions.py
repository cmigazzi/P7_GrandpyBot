
class InvalidQuestionException(Exception):

    def __init__(self):
        self.name = "Invalid Question"


class NoSpacesException(Exception):

    def __init__(self):
        self.name = "No spaces"


class NotGeographicException(Exception):

    def __init__(self):
        self.name = "Not geographic"


class NotEnoughWordsException(Exception):

    def __init__(self):
        self.name = "Not enough words"
