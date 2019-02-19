
from grandpy.response_provider import ResponseProvider
from grandpy.responses import RESPONSES


def test_class_exists():
    rp = ResponseProvider()
    assert rp


def test_welcome():
    rp = ResponseProvider()
    assert rp.welcome() in RESPONSES["welcome"]


def test_misunderstood():
    rp = ResponseProvider()
    assert rp.misunderstood() in RESPONSES["misunderstood"]


def test_understood():
    rp = ResponseProvider()
    assert rp.understood() in RESPONSES["understood"]
