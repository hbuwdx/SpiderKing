class Task:

    def __init__(self, task_id, url, priority):
        self.task_id = task_id
        self.url = url
        self.priority = priority


class TaskQueue:

    def __init__(self):
        self.tasks = []

    def append(self, task):
        # for i in range(len(self.tasks)):
        #     if task.url == self.tasks[i].url:
        #         return
        self.tasks.append(task)

    def pop(self):
        if self.length() > 0:
            return self.tasks.pop()

    def length(self):
        return len(self.tasks)