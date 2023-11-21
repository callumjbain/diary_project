import pytest
from lib.task_tracker import *

"""
    Given a task as a string 
    It is added to the list
    def add_task(This is a task) -> task added to the list
"""
def test_add_a_single_task():
    task_tracker = TaskTracker()
    task_tracker.add("Wash the dishes")
    expected = ["Wash the dishes"]
    actual = task_tracker.task_list
    assert actual == expected

"""
    Given a task is empty
    Raise an exception 
    def add_task("") -> "Please add a task"
"""
def test_add_an_empty_task():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e: 
        task_tracker.add("")
    error_message = str(e.value)
    assert error_message == "Please add a task"

def test_show_list():
    task_tracker = TaskTracker()
    task_tracker.add("Wash the dishes")
    expected = ["Wash the dishes"]
    actual = task_tracker.show_list()
    assert actual == expected

def test_removal_of_task():
    task_tracker = TaskTracker()
    task_tracker.add("Wash the dishes")
    task_tracker.add("Hang the washing")
    task_tracker.add("Make the bed")
    task_tracker.add("Paint the house")
    task_tracker.task_removal("Wash the dishes")
    expected = ["Hang the washing", "Make the bed", "Paint the house"]
    actual = task_tracker.task_list
    assert expected == actual

def test_removal_of_task_with_empty_list():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.task_removal("Wash the dishes")
    error_message = str(e.value)
    assert error_message == "You have nothing in your list."
    
def test_remove_task_thats_not_in_list():
    task_tracker = TaskTracker()
    task_tracker.add("Wash the dishes")
    task_tracker.add("Hang the washing")
    task_tracker.add("Make the bed")
    task_tracker.add("Paint the house")
    with pytest.raises(Exception) as e:
        task_tracker.task_removal("Wash the car")
    error_message = str(e.value)
    assert error_message == "This task is not in your list."

def test_initialiser():
    music = MusicTracker()
    assert isinstance(music, MusicTracker)

def test_adding_new_music():
    music = MusicTracker()
    music.add("Simply The Best")
    expected = ["Simply The Best"]
    actual = music.music_list
    assert expected == actual

def test_adding_new_music_is_empty():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.add("")
    error_message = str(e.value)
    assert error_message == "Please add a song."

def test_adding_new_music_is_empty():
    music = MusicTracker()
    music.add("Simply The Best")
    with pytest.raises(Exception) as e:
        music.add("Simply The Best")
    error_message = str(e.value)
    assert error_message == "This song has already been added."

def test_shows_list_of_music():
    music = MusicTracker()
    music.add("Simply The Best")
    music.add("I Want To Break Free")
    music.add("Billie Jean")
    music.add("Gravity")
    expected = ["Simply The Best", "I Want To Break Free","Billie Jean", "Gravity"]
    actual = music.show_songs()
    assert expected == actual

def test_list_is_empty():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.show_songs()
    error_message = str(e.value)
    assert error_message == "You have no music in your list."