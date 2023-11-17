#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
cities of that state, using the database """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id  = state_id\
                    WHERE states.name = %s;"
                .format(argv[4]))

    for row in cur.fetchall():
        cities += f"{row[0]}, "
    cur.close()
    db.close()
