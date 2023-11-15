def is_grammar_correct(str):
    if str[0].istitle():
        if str[-1] == ".":
            return "Your grammar is correct."
        else:
            return "This needs a full stop."
    else:
        return "This needs a capital letter."
    
