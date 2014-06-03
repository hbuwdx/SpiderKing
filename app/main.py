from logic.download import ThreadPool
from logic.queue import *
from logic.manager import *
from spider.spider import Spider


if __name__ == "__main__":
    print("the application starts on ...")

    task_queue = TaskQueue()
    start_task = Task(1, "http://news.baidu.com/", 0)
    task_queue.append(start_task)

    thread_pool = ThreadPool(50, 60)

    manager = Manager(task_queue, thread_pool)
    Spider.manager = manager
    manager.start()