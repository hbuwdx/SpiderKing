from logic.download import ThreadPool
from logic.queue import *
from logic.manager import *
from spider.spider import Spider


if __name__ == "__main__":
    print("the application starts on ...")

    task_queue = TaskQueue()
    # task = Task(1, "http://www.cnblogs.com/2gua/archive/2012/09/03/2668125.html", 0)
    # task_queue.append(task)

    task2 = Task(1, "http://news.baidu.com/", 0)
    task_queue.append(task2)

    thread_pool = ThreadPool(50, 60)

    manager = Manager(task_queue, thread_pool)
    Spider.manager = manager
    manager.start()