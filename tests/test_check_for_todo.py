import pytest
from lib.check_for_todo import *

def test_check_for_todo_true():
    result = check_for_todo('Here is a task #TODO')
    assert result == True

def test_check_for_todo_false():
    result = check_for_todo('Here is a task')
    assert result == False

def test_check_for_todo_empty():
    with pytest.raises(Exception) as e:
        check_for_todo()
    error_message = str(e.value)
    assert error_message == "check_for_todo() missing 1 required positional argument: 'str'"