import pytest


@pytest.fixture()
def setup():
    print("setup")
    yield
    print("teardown")
