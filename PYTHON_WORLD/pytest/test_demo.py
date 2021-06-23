import pytest


def test_1():
    hi = 'hello'
    assert hi == 'hey', 'did not match'

@pytest.mark.smoke
def test_3():
    a = 2
    assert a+2 == 4, "not equal"
