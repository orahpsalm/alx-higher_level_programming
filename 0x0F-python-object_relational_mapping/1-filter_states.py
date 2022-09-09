#!/usr/bin/python3
"""Lists all the states that start with letter "N" from the db"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    res = cur.fetchall()
    for r in res:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    db.close()
