import threading
import queue

class TaskQueue:
    def __init__(self):
        self.__lock = threading.Lock() 
        self.__condi = threading.Condition(self.__lock)
        self.__tasks_queue = queue.Queue()
        self.__tasks_to_do = queue.Queue()
        self.__stop = True 

    def run(self):
        print ('task queue is running')

        self.__stop = false 
        while True:
            if self.__stop == True:
                break

            try:
                self.__lock.acquire()
                while self.__tasks_queue.empty():
                    if self.__stop == True:
                        break
                    self.__condi.wait()

                if self.__stop == True:
                    break

                #fetch tasks from queue and put them in the to do queue
                while !self.__tasks_queue.empty():
                    self.__tasks_to_do.put(self.__tasks_queue.get())
            finally:
                self.__lock.release()

            if self.__stop == True:
                break

            while !self.__tasks_to_do.empty():
                if self.__stop == True:
                    break
                task = self.__task_to_do.get()
                if callable(task):
                    task()

    def push_task(self, task):
        try:
            self.__lock.acquire()
            self.__tasks_queue.put(task)
            cond.notify()
        finally:
            self.__lock.release()

    def stop(self):
        self.__stop = True

    
