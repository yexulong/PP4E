#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import os
import time


def counter(count):
    for j in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), j))


for i in range(5):
    pid = os.spawnv()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)
print('Main process exiting.')