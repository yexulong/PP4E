#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
"""windows 不能用"""
import os


def child():
    print('Hello from child', os.getpgid())
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpgid(), newpid)
        if input() == 'q':
            break


parent()
