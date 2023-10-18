import pytest

from fuel import convert, gauge

# pytest.raises(ZeroDivisionError):


# convert a string as x/y and convert  a percentage
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99


# gauge => expect an int and returns e , f or percentage
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_error():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
