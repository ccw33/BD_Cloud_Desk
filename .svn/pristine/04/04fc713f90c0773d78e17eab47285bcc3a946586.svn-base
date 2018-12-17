#encoding:utf-8
import threading

import time


def queue_threads_worker(q,func):
    while not q.empty():
        data = q.get()
        func(*data[0],**data[1])
        q.task_done()#任务完成，告诉q一声


# MyThread.py线程类

class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            threading.Thread.join(self)  # 等待线程执行完毕
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return

