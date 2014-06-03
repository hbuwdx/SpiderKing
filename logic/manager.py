from logic.download import *


class Manager(object):
    def __init__(self, task_queue, thread_pool):
        self.task_queue = task_queue
        self.thread_pool = thread_pool

    def start(self):
        while True:
            if self.task_queue.length > 0:
                thread = self.thread_pool.get_a_thread()
                thread.do_task(self.task_queue.pop())
            time.sleep(1)