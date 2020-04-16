#!/usr/bin/python3
import sys, signal, time

def now():
    return time.ctime(time.time())              # 当前时间的字符串

def onSignal(signum, stackframe):               # python信号处理器
    print('Got signal', signum, 'at', now())    # 多数信号处理器一直有效

signum = int(sys.argv[1])
signal.signal(signum, onSignal)                 # 布置信号处理器
while True:
    signal.pause()                              # 等待信号(或pass)
 
