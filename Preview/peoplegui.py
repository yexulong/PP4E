"""
实现一个图形界面，用于查看和更新存储于shelve中的类实例；
该shelve保存在脚本运行的机器上，可能是一个或多个本地文件
"""
from tkinter import *
from tkinter.messagebox import showerror
import shelve


shlvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for(ix, label) in enumerate(('key',) +fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=LEFT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from person_alternative import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
        print('success!')
        db[key] = record


db = shelve.open(shlvename)
window = makeWidgets()
window.mainloop()
db.close()  # 程序退出或窗口关闭时，程序执行返回到这里
