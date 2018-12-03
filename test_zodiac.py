from zodiac import *
import pytest

def test_zodiac_input(monkeypatch):
    with monkeypatch.context() as m:
        ## First Test
        m.setattr('builtins.input', lambda x: "1231")
        date = zodiac_input()
        assert date == '1231'
        ## Second test
        m.setattr('builtins.input', lambda x: "0101")
        date = zodiac_input()
        assert date == '0101'

def test_get_zodiac(monkeypatch):
    with monkeypatch.context() as m:
        ## First Test
        m.setattr('builtins.input', lambda x: "0101")
        zodiac = get_zodiac()
        assert zodiac == 'Sagittarius'
        ## Second Test
        m.setattr('builtins.input', lambda x: "0810")
        zodiac = get_zodiac()
        assert zodiac == 'Leo'