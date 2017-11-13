# Praveen Lama
# IS 211
# Assignment 10
# Fall 2017

import sqlite3


def main():

    conn = sqlite3.connect("pets.db")  # initializing db connection
    cur = conn.cursor()

    # these are the series of tasks been performed in db

    # check if there the table exists and if true delete them
    cur.execute('DROP TABLE IF EXISTS person')
    cur.execute('DROP TABLE IF EXISTS pet')
    cur.execute('DROP TABLE IF EXISTS person_pet')

    # create new tables
    cur.execute('''CREATE TABLE person (
                     id INTEGER PRIMARY KEY,
                     firstName TEXT,
                     lastName TEXT,
                     age INTEGER )
              ''')
    cur.execute('''CREATE TABLE pet (
                     id INTEGER PRIMARY KEY,
                     name TEXT,
                     breed TEXT,
                     age INTEGER,
                     dead INTEGER );
              ''')
    cur.execute('''CREATE TABLE person_pet (
                     personId INTEGER,
                     pet_id INTEGER );
              ''')

    # inserting records into tables
    cur.execute('''INSERT INTO person
                     (id, firstName, lastName, age)
                 VALUES
                     (1, "James", "Smith", 41),
                     (2, "Diana", "Greene", 23),
                     (3, "Sara", "White", 27),
                     (4, "William", "Gibson", 23)
              ''')
    cur.execute('''INSERT INTO pet
                     (id, name, breed, age, dead)
                 VALUES
                     (1, "Rusty", "Dalmation", 4, 1),
                     (2, "Bella", "Alaskan Malamute", 3, 0),
                     (3, "Max", "Cocker Spaniel", 1, 0),
                     (4, "Rocky", "Beagle", 7, 0),
                     (5, "Rufus", "Cocker Spaniel", 1, 0),
                     (6, "Spot", "Bloodhound", 2, 1)
              ''')
    cur.execute('''INSERT INTO person_pet
                     (personId, pet_id)
                 VALUES
                     (1, 1),
                     (1, 2),
                     (2, 3),
                     (2, 4),
                     (3, 5),
                     (4, 6)
              ''')

    # now ready to execute the commands
    conn.commit()

    conn.close()

    print " Finished Successfully loading all the documents"

if __name__ == "__main__":
    main()