import pytest


@pytest.mark.smoke
def test_2():
    i = 'hi'
    assert i == 'hey', "not equal"
