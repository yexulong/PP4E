#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import sys


def filter_files(name, function):
    with open(name, 'r') as input_f, open(name + '.out', 'w') as output_f:
        for line in input_f:
            output_f.write(function(line))


def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')


if __name__ == '__main__':
    filter_stream(lambda line: line)
