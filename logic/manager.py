import threading
import time
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
    def get_status():
        while True:
            time.sleep(2)
            print("-------------------------status---------------------------------------")
            print("have done urls : size[" + gl.done_urls.__len__().__str__() + "]")
            print("have done urls : mem size[" + gl.done_urls.__sizeof__().__str__() + "]")
            print("todo urls :  size[" + gl.db.collection("todo_urls").count().__str__() + "]")
            print("done urls :  size[" + gl.db.collection("urls").count().__str__() + "]")
            print("todo_urls counts" + gl.db.collection("count").find({"name": "todo_urls"})[0]["count"].__str__())
            print("urls counts" + gl.db.collection("count").find({"name": "urls"})[0]["count"].__str__())

    @staticmethod
    def start():
        threading.Thread(target=Manager.get_task).start()
        threading.Thread(target=Manager.get_status).start()
        while True:
            if gl.task_queue.length() > 0:
                thread = gl.thread_pool.get_a_thread()
                thread.do_task(gl.task_queue.pop())