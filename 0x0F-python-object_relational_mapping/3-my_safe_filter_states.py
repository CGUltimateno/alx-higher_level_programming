#!/usr/bin/python3
""" Script that lists all states from the database """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states
                WHERE BINARY
                name = %s;""", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
