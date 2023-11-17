#!/usr/bin/python3
""" Script that Lists all cities with the
states they belong to
from the database hbtn_0e_4_usa """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
