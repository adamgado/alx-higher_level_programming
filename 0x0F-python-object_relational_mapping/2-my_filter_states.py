#!/usr/bin/python3
"""lists states from database matching argument"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """get the states from the database"""
    db_list = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])
    x = db_list.cursor()
    x.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
              .format(sys.argv[4]))
    states_db = x.fetchall()
    for a in states_db:
        print(a)