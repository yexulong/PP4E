#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM    # 可移植的套接字api

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)  # 允许最多5个等待中的客户端
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s]' % data
        conn.send(reply.encode())

def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)                        # 从监听者哪里接受字节数据
    sock.close()                                   # 消息最多包含1024字节
    print('client got: [%s]' % reply)

if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True                          # 不等待服务器线程
    sthread.start()                                # 等待子线程结束
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()
