import threading
import gl
from logic.queue import *


class Manager(object):

    @staticmethod
    def get_task():
        while True:
            url = gl.db.collection(gl.DB_TODO_URLS_NAME).find_one()
            if url:
                task = Task(1, url["url"].__str__(), 1)
                gl.task_queue.append(task)
                gl.db.collection(gl.DB_TODO_URLS_NAME).remove(url)

    @staticmethod
    def start():
        threading.Thread(target=Manager.get_task).start()
        while True:
            if gl.task_queue.length() > 0:
                thread = gl.thread_pool.get_a_thread()
                thread.do_task(gl.task_queue.pop())