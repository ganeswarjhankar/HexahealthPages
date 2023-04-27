import pytest

@pytest.mark.login
def test_m1():
    a=2
    b=4
    assert a+2==b,"print a"
    assert a==b,"print b"

def test_m2():
    name="selenium"
    assert name.upper()=="SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert True

def test_m5():
    assert 100==100
def test_m6():
    assert "naveen"=="naveen"

def test_login_FB():
    assert "admin"=="admin"

