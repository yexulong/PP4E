#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import _thread as thread
import time


def counter(myId, count):
    for j in range(count):
        time.sleep(1)
        mutex.acquire()
        print('[%s] => %s' % (myId, j))
        mutex.release()


mutex = thread.allocate_lock()
for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print('Main thread exiting.')
