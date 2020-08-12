import shelve


with shelve.open('class-shelve') as db:
    for key in db:
        print(key, '=>\n    ', db[key].name, db[key].pay)
    bob = db['bob']
    print(bob.lastName())
    print(db['tom'].lastName())
