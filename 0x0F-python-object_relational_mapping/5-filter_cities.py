#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
cities of that state, using the database """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT ct.id, ct.name FROM cities ct LEFT JOIN
    states st ON st.id = ct.state_id WHERE st.name=%s  ORDER BY ct.id ASC"""
                .format(argv[4]))
    print(', '.join([rec[1] for rec in cur.fetchall()]))
    cur.close()
    db.close()
