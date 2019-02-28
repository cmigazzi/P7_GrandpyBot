"""Contains question types."""

from enum import Enum


class QuestionType(Enum):
    """Enumerate all the type of question."""

    STANDARD = 1
    FORMAL = 2
    COLLOQUIAL = 3
    W_WORD = 4
    KEYWORDS_FIRST = 5
