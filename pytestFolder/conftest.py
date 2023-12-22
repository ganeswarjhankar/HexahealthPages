import pytest

@pytest.fixture(scope='session',autouse=True)

def myfixture():
    print("conftest is called")