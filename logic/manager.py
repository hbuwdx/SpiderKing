class Manager(object):
    def __init__(self, task_queue, thread_pool):
        self.task_queue = task_queue
        self.thread_pool = thread_pool
        self.running = True

    def start(self):
        while self.running:
            if self.task_queue.length() > 0:
                thread = self.thread_pool.get_a_thread()
                thread.do_task(self.task_queue.pop())