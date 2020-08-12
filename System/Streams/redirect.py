#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import sys


class Output:                               # 模拟输出文件
    def __init__(self):
        self.text = ''                      # 新建空字符串

    def write(self, string):                # 添加字节字符串
        self.text += string

    def writelines(self, lines):            # 在列表中添加每一行数据
        for line in lines:
            self.write(line)


class Input:                                # 模拟输入文件
    def __init__(self, input_=''):           # 默认参数
        self.text = input_                   # 保存新建的字符串

    def read(self, size=None):              # 可选参数
        if size is None:                    # 读取N个字节，或者所有字节
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res

    def readline(self):
        eoln = self.text.find('\n')         # 查找下一个eoln的偏移位置
        if eoln == -1:                      # 清洗eoln,其值为01
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res


def redirect(function, pargs, kargs, input_):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input_)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
    return result, output
