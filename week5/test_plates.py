import pytest
from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("AA") == True


def test_invalid():
    assert is_valid("A2") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("2A") == False
    assert is_valid(" 2") == False
    assert is_valid("22") == False

    assert is_valid("OUTATIME") == False
