#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
cities of that state, using the database """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name\
                    FROM cities\
                    LEFT JOIN states\
                    ON cities.state_id  = states.id\
                    WHERE states.name = %s; ORDER by cities.id"
                .format(argv[4]))

    print(', '.join([rec[1] for rec in cur.fetchall()]))
    cur.close()
    db.close()
