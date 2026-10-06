from lib.count_words import *
import pytest

def test_word_count_is_correct():
    assert count_words("how many words in this string?") == 6

def test_empty_string_is_zero():
    assert count_words("") == 0

def test_space_is_zero():
    assert count_words(" ") == 0

def test_integer_raises_error():
    with pytest.raises(AttributeError) as e:
        count_words(3)
    error = str(e.value)
    assert error == "Argument must be a string"

def test_works_with_commas():
    assert count_words("hello,there,i,write,like,this") == 6