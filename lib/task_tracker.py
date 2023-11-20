class TaskTracker():

    def __init__(self):
        self.task_list = []

    def add(self, new_task):
        if new_task == "":
            raise Exception("Please add a task")
        self.task_list.append(new_task)

    def show_list(self):
        return self.task_list 

# task_tracker = TaskTracker()
# task_tracker.add("Wash the dishes")

# print(task_tracker.task_list)