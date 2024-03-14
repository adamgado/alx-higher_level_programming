#!/usr/bin/python3
"""lists all states from database"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db_list = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])
    x = db_list.cursor()
    x.execute("SELECT * FROM states")
    states_db = x.fetchall()
    for a in states_db:
        print(a)
