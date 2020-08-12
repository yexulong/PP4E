#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler


webdir = '.'    # 存放HTML文件和cgi-bin脚本文件夹的所在
port = 80

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
