"""Contains all the customs exceptions."""


class InvalidQuestionException(Exception):
    """Exception when question is invalid."""

    def __init__(self):
        """Define name."""
        self.name = "Invalid Question"


class NoSpacesException(Exception):
    """Exception when no space in question."""

    def __init__(self):
        """Define name."""
        self.name = "No spaces"


class NotGeographicException(Exception):
    """Exception when question is not geographic."""

    def __init__(self):
        """Define name."""
        self.name = "Not geographic"


class NotEnoughWordsException(Exception):
    """Exception when there is not enough words."""

    def __init__(self):
        """Define name."""
        self.name = "Not enough words"


class ZeroResultException(Exception):
    """Exception when there is no result."""

    def __init__(self):
        """Define name."""
        self.name = "Zero result"
