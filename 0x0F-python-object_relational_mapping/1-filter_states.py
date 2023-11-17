#!/usr/bin/python3
""" Script that lists all states from the database
   that start with N """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(user=argv[1],
                         passwd=argv[2], db=argv[3])\
                         as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT id, name FROM states
            WHERE name 
            LIKE BINARY 'N%'""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
