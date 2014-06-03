import threading
import time
from spider.spider import Spider


class DownloadThread(threading.Thread):

    def __init__(self, thread_id):
        super(DownloadThread, self).__init__(group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
        self.id = thread_id
        self.working = False
        self.task = None
        self.start()

    def do_task(self, task):
        if task and task.url:
            print("[thread:"+self.id.__str__()+"] do task["+task.url+"]\n")
            self.task = task

    def run(self):
        while True:
            if self.task:
                self.working = True
                Spider.fetch(self.task.url)
                self.task = None
            self.working = False
            time.sleep(1)
            print(self.id.__str__()+"wating a task ...\n")


class ThreadPool:
    def __init__(self, min_num=2, max_num=20):
        self.min_num = min_num
        self.max_num = max_num
        self.threads = []
        self.__create_thread()

    def __create_thread(self):
        if self.min_num > self.max_num:
            print("min num can not be larger than max num")
        for i in range(self.min_num):
            self.threads.append(DownloadThread(i))
            print("create thread:" + i.__str__())

    def num_of_not_working_thread(self):
        not_working_num = 0
        for i in range(len(self.threads)):
            if not self.threads[i].working:
                not_working_num += 1
        return not_working_num

    def __get_a_not_working_thread_id(self):
        for i in range(len(self.threads)):
            if not self.threads[i].working:
                return i
        return -1

    def get_a_thread(self):
        thread_id = self.__get_a_not_working_thread_id()
        if thread_id == -1:
            thread_len = len(self.threads)
            if thread_len < self.max_num:
                new_thread_id = thread_len + 1
                self.threads.append(DownloadThread(new_thread_id))
                return self.threads[new_thread_id]
            else:
                time.sleep(1)
                return self.get_a_thread()
        else:
            return self.threads[thread_id]