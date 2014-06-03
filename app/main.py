from logic.queue import *
from logic.manager import *


if __name__ == "__main__":
    print("the application starts on ...")

    task_queue = TaskQueue()
    task = Task(1, "http://www.cnblogs.com/2gua/archive/2012/09/03/2668125.html", 0)
    task_queue.append(task)

    thread_pool = ThreadPool()

    manager = Manager(task_queue, thread_pool)
    Spider.manager = manager
    manager.start()
