#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-


def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line)
    file.close()
