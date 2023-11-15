from lib.make_snippet import *

def test_make_snippet1():
    result = make_snippet("the cat and this dog are in the garden")
    assert result == "the cat and this dog..."

def test_make_snippet2():
    result = make_snippet("the cat")
    assert result == "the cat..."