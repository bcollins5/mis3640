import dbm
import random

def create_db():
    '''
    return a new database containing names and 0s
    '''


    ROSTER = ("Beshansky",
            "Collins",
            "Fischer",
            "Giovanucci",
            "Jain",
            "Kim",
            "Lauture",
            "Lee",
            "Maddox",
            "Martinez",
            "Mendez",
            "Oh",
            "Petrone",
            "Posada",
            "Rule",
            "Schilb",
            "Tariq",
            "Wang",
            "Wolf")
    visits = ['0']
    db = dbm.open('db_student', 'c')
    for student in ROSTER:
        db[student] = random.choice



def call(db_name):
    '''
 
 
 
 def display_student:
    db = dbm.open('db_student', 'c')
    for student in ROSTER:
        db[student] = random.choice(GRADES)
    for key in db:
        print(key, db[key])


db.close()