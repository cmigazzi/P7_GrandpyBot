"""Contains tests suite for ResponseProvider."""

from grandpy.response_provider import ResponseProvider
from grandpy.responses import RESPONSES
from grandpy.parser.exceptions import (InvalidQuestionException,
                                       NoSpacesException,
                                       ZeroResultException)


def test_class_exists():
    """Test class exist."""
    rp = ResponseProvider()
    assert rp


def test_exception():
    """Test exception catch."""
    rp = ResponseProvider(InvalidQuestionException())
    assert rp.exception == "Invalid Question"


def test_provider():
    """Test provider() method."""
    rp = ResponseProvider()
    assert rp.provider() in RESPONSES["welcome"]


def test_interrogation_mark():
    """Test no_interrogation_mark() method."""
    rp = ResponseProvider(InvalidQuestionException())
    assert rp.provider() in RESPONSES["interrogation_mark"]


def test_spaces():
    """Test no_spaces() method."""
    rp = ResponseProvider(NoSpacesException())
    assert rp.provider() in RESPONSES["no_spaces"]


def test_zero_result():
    """Test zero_result() method."""
    rp = ResponseProvider(ZeroResultException())
    assert rp.provider() in RESPONSES["zero_result"]
