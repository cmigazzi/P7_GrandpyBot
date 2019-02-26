
from grandpy.response_provider import ResponseProvider
from grandpy.responses import RESPONSES
from grandpy.parser.exceptions import (InvalidQuestionException,
                                       NoSpacesException,
                                       ZeroResultException)


def test_class_exists():
    rp = ResponseProvider()
    assert rp


def test_welcome():
    rp = ResponseProvider()
    assert rp.provider() in RESPONSES["welcome"]


def test_exception():
    rp = ResponseProvider(InvalidQuestionException())
    assert rp.exception == "Invalid Question"


def test_provider():
    rp = ResponseProvider()
    assert rp.provider() in RESPONSES["welcome"]


def test_interrogation_mark():
    rp = ResponseProvider(InvalidQuestionException())
    assert rp.provider() in RESPONSES["interrogation_mark"]


def test_spaces():
    rp = ResponseProvider(NoSpacesException())
    assert rp.provider() in RESPONSES["no_spaces"]


def test_zero_result():
    rp = ResponseProvider(ZeroResultException())
    assert rp.provider() in RESPONSES["zero_result"]
