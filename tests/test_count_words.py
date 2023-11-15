from lib.count_words import *

def test_count_words():
    result = count_words("Geeksforgeeks is best Computer Science Portal")
    assert result == 6