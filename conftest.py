import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executed first ")
    yield
    print("i will be executed last")


def dataLoad():
    print("i will be executed later")
    return ["Ganeswar","Lucky"]

