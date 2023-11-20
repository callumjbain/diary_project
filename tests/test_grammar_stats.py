from lib.grammar_stats import *


# test to see if the first letter is capitalised.
def test_letter_is_capitalized_and_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This text has a capital letter.")
    assert result == True

def test_letter_is_capitalized():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This text has a capital letter")
    assert result == False

def test_percentage_of_true():
    grammar_stats = GrammarStats()
    grammar_stats.check("This text has a capital letter.")
    grammar_stats.check("This text has a capital letter and a full stop.")
    grammar_stats.check("This text has a capital letter and a full stop and is longer.")
    result = grammar_stats.percentage_good()

    assert result == 100
