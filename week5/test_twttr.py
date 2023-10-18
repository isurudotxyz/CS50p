import pytest
from twttr import shorten


def testing_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    # try:
    #     if shorten("ciao") == "c":
    #         return True
    #     else:
    #         raise KeyError
    # except:
    #     sys.exit("vowels not omitted")


def testing_number():
    assert shorten("098") == ("098")


def testing_symbol():
    assert shorten("*//[]}") == "*//[]}"

    # try:
    #     if shorten("*//[]") == "*//[]":
    #         return True
    #     else:
    #         raise KeyError
    # except:
    #     sys.exit("symbol omitted")
