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
