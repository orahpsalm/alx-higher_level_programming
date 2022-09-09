#!/usr/bin/python3
"""Module which lists all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    res = cur.fetchall()
    for r in res:
        print(r)
    cur.close()
    db.close()
