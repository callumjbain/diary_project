import pytest

from lib.correct_grammar import *

def test_correct_grammar1():
    result = is_grammar_correct("This sentence is correct.")
    assert result == "Your grammar is correct."

def test_correct_grammar_no_caps():
    result = is_grammar_correct("this sentence has no capital letter.")
    assert result == "This needs a capital letter."

def test_correct_grammar_no_stop():
    result = is_grammar_correct("This sentence has no full stop")
    assert result == "This needs a full stop."

def test_correct_grammar_empty_string():
    with pytest.raises(Exception) as e:
        is_grammar_correct("")
    error_message = str(e.value)
    assert error_message == "string index out of range"

def test_correct_grammar_no_input():
    with pytest.raises(Exception) as e:
        is_grammar_correct()
    error_message = str(e.value)
    assert error_message == "is_grammar_correct() missing 1 required positional argument: 'str'"