class TaskTracker():

    def __init__(self):
        self.task_list = []

    def add(self, new_task):
        if new_task == "":
            raise Exception("Please add a task")
        self.task_list.append(new_task)

    def show_list(self):
        return self.task_list 
    

    def task_removal(self, task_to_remove):
        if self.task_list == []:
            raise Exception("You have nothing in your list.")
        if task_to_remove not in self.task_list:
            raise Exception("This task is not in your list.")
        self.task_list.remove(task_to_remove)
        return self.task_list


class MusicTracker():
    def __init__(self):
        self.music_list = []

    def add(self, new_music):
        if new_music == "":
            raise Exception("Please add a song.")
        if new_music in self.music_list:
            raise Exception("This song has already been added.")
        self.music_list.append(new_music)

    def show_songs(self):
        if self.music_list == []:
            raise Exception("You have no music in your list.")
        return self.music_list
    
