# Exercise One

1.Descibe the problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

# 2. Design the Function Signature

def __init__(self) 
    music_list []

def add(self, new_music)
returns : nothing
side effects: add music to our list

def show_songs(self)
returns: list
side effects: none

# 3. Create Examples as Tests

    Given no input
    Test that init statemnt is valid
    def test_init()

    Given new music as a string
    This is then added to music list
    def add(new music) => new music added to list

    Given new music is an empty string
    Raise error message
    def add(nothing) => error message raised

    Given new music as a string
    If new music is already in list, rasises error message
    def add(new music) => if new music already in - raise error message

    Given music_list has items in list
    Returns music_list
    def show_songs() => returns list of songs

    Given music_list is empty
    Returns error message
    def show_songs() => returns error message



# 4. Implement Their Behaviour 