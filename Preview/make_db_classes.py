import shelve
from person_alternative import Person
from person_alternative import Manager


bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

with shelve.open('class-shelve') as db:
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
