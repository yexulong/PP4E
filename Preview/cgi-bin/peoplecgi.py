#!C:\Users\wb.yexulong\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import cgi
import html
import os
import shelve
import sys

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

#  主html模板
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
<p>
    <input type=submit value="Fetch" name=action>
    <input type=submit value="Update" name=action>
</form>
</body>
</html>
"""

# 为$ROWS$的数据行插入html
rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname, ) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)


def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = html.escape(repr(value))
    return new


def fetcgRecord(db_a, form_a):
    try:
        key = form_a['key'].value
        record = db_a[key]
        fields_a = record.__dict__
        fields_a['key'] = key
    except:
        fields_a = dict.fromkeys(fieldnames, '?')
        fields_a['key'] = 'Missing or invalid key!'
    return fields_a


def updateRecord(db_a, form_a):
    if not 'key' in form_a:
        fields_a = dict.fromkeys(fieldnames, '?')
        fields_a['key'] = 'Missing key input!'
    else:
        key = form_a['key'].value
        if key in db_a:
            record = db_a[key]
        else:
            from person_alternative import Person
            record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(form_a[field].value))
        db_a[key] = record
        fields_a = record.__dict__
        fields_a['key'] = key
    return fields_a


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetcgRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))
