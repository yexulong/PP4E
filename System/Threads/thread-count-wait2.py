#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import _thread as thread


stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10


def counter(myId, count):
    for j in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, j))
        stdoutmutex.release()
    exitmutexes[myId] = True


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

while False in exitmutexes:
    pass
print('Main thread exiting.')
