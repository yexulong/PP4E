#!/usr/bin/python3

import sys, signal, time

def now():
    return time.asctime()

def onSignal(signum, stackframe):
    print('Got alarm', signum, 'at', now())    

while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal)         # 布置信号处理器
    signal.alarm(5)                                 # 5秒后发送信号
    signal.pause()                                  # 等待信号
