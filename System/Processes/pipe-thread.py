#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import os
import threading
import time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)