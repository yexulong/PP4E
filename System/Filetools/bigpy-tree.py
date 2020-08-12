#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import sys, os, pprint


trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\lib'
else:
    dirname = '/usr/lib/python'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
