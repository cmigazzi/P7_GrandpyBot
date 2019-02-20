
class InvalidQuestionException(Exception):
    
    def __init__(self):
        self.name = "Invalid Question"

class NoSpacesException(InvalidQuestionException):
    
    def __init__(self):
        self.name = "No spaces"