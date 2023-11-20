# Exercise One

1.Descibe the problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

# 2. Design the Function Signature

def add_task()

Parameter: Tasks as strings

Returns: adds task to the list

Side effects: None, o

def task_list()

Parameter: None

Returns: Returns the list

def task_removal()

Parameter: Tasks as strings

Returns: new list without the removed task

Side effects: None, o

# 3. Create Examples as Tests

    Given a task as a string 
    It is added to the list
    def add_task(This is a task) -> task added to the list

    Given a task is empty
    Raise an exception 
    def add_task("") -> "Please add a task"

    Given items have been added to the list
    It returns the list
    def task_list() => list of items

    Give an empty list
    Raise an exception 
    def task_list('') => "You haven't added anything just yet"

    Given item has been removed from the list
    print the list without the removed item
    def remove_task("The task to remove") -> new list without the task

# 4. Implement Their Behaviour 