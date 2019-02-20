
from grandpy.response_provider import ResponseProvider
from grandpy.responses import RESPONSES
from grandpy.parser.exceptions import InvalidQuestionException, NoSpacesException


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
