# Praveen Lama
# IS 211
# Assignment 10
# Fall 2017

import sqlite3

# What is the purpose of the person_pet table?
# Answer: The person_table acts as an intermediary table between person and pet table. In Database terms,
#         it is Normalization where we split large tables into small ones and define relationship between them.

def main():

    conn = sqlite3.connect("pets.db")  # initializing db connection
    cur = conn.cursor()

    personId = 0
    while personId != -1:
        try:
            personId = int(raw_input("Enter an ID number: "))
            cur.execute('SELECT firstName, lastName, age FROM person WHERE id = %i' % personId)
            personData = cur.fetchone()
            personName = "%s %s" % (personData[0], personData[1])
            personAge = personData[2]
            print " %s, %i years old" % (personName, personAge)

            # sql join performed to reference between person and pet via ID
            cur.execute('''SELECT person.firstName, person.lastName, pet.name,
                          pet.breed, pet.age, pet.dead
                         FROM pet
                         LEFT JOIN person_pet
                         ON pet.id = person_pet.pet_id
                         LEFT JOIN person
                         ON person_pet.personId = person.id
                         WHERE person.id = %i
                      ''' % personId)

            pet_list = cur.fetchall()
            for pet in pet_list:
                petName = pet[2]
                petBreed = pet[3]
                petAge = pet[4]
                petDead = pet[5]

                if petDead == 0:
                    print " %s owns %s, a %s, that is %s" % \
                          (personName, petName, petBreed, petAge)
                elif petDead == 1:
                    print " %s owned %s, a %s, that was %s" % \
                          (personName, petName, petBreed, petAge)
        except ValueError:
            print "Only Integers are allowed as input"
        except TypeError:
            if personId == -1:
                conn.close()
                print " Exiting program."
                exit(-1)
            print " No Data found with that ID."


if __name__ == "__main__":
    main()