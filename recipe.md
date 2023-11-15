<!-- # Exercise One

# 1.Descibe the problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# 2. Design the Function Signature

    def words_per_minute()

    Parameters: String -   a string of any length. 

    Returns: Number of minutes as integer.

    Side Effects: Print output. 

# 3. Create Examples as Tests
    Given a 200 word string.
    It returns one minute to read.
    words_per_minute("200 words...") => (1)

    Given a 400 word string.
    It returns two minutes to read.
    words_per_minute("400 words...") => (2)

    Given a 100 word string.
    It returns half a minute to read.
    words_per_minute("100 words...") => (0.5)


# 4. Impliment Their Behaviour 
    See file named... 
-->


<!-- Exercise Two

 1.Descibe the problem
    As a user
    So that I can improve my grammar
    I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

 
 2. Design the Function Signature
    def is_grammar_correct(str)

    Parameters - String

    Returns - "Your grammar is correct" if letter is capitalised and full stop is at end. OR "Your grammar in incorrect" if these are not the case.

    Side effects - prints out result statement
 
 3. Create Examples as Tests

    Give sentnce with correct grammar. "This sentence is correct."
    Returns "Your grammar is correct"
    is_grammar_correct('string') => "Your grammar is correct."

    Give sentnce with No capital letter. "this sentence has no capital letter."
    Returns "This needs a capital letter."
    is_grammar_correct('string') => "This needs a capital letter."

    Give sentnce with no full stop. "This sentence has no full stop"
    Returns "This needs a full stop."
    is_grammar_correct('string') => "This needs a full stop."

    Don't give any input.
    Returns "No input given"
    is_grammar_correct(None) => "No input given."
 
 4. Impliment Their Behaviour 
 
 
 
 
 -->