#!/usr/bin/python3
import os, time, sys
fifoname = '/tmp/pipefifo'

def child():
    pipeout = os.open(fifoname, os.O_WRONLY)    # 作为文件描述符打开FIFO
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5

def parent():
    pipein = open(fifoname, 'r')                # 作为文本文件对象打开FIFO
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()                                # 如果没有参数则作为父进程运行
    else:
        child()                                 # 否则作为子进程运行
