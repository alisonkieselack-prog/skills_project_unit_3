from lib.diary import *

def test_less_than_5_returns_same_thing():
    assert make_snippet("there are four words") == "there are four words"

def test_5_returns_same_thing():
    assert make_snippet("there are five words now") == "there are five words now"

def test_over_5_returns_same_thing():
    assert make_snippet("there are much more than five words in here now") == "there are much more than..."