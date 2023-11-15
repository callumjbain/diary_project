<!-- # Exercise One

# 1.Descibe the problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

# 2. Design the Function Signature

def check_for_todo()

Parameter: Tasks as strings

Returns: boolean value, true if contains #TODO

Side effects: None, only boolian return

# 3. Create Examples as Tests

    Given a string that contains a #TODO
    It returns True
    def check_for_todo('Here is a task #TODO') => True

    Give a string doesn't contain a #TODO
    It returns False
    def check_for_todo('Here is a task') => False

    Give an empty string
    It returns error message
    def check_for_todo('') => Error message

# 4. Impliment Their Behaviour 