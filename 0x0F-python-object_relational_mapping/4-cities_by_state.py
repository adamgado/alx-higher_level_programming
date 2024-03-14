#!/usr/bin/python3
"""lists cities from database"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """get the states from the database"""
    db_list = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])
    x = db_list.cursor()
    x.execute("""SELECT cities.id, cities.name, states.name FROM
              cities INNER JOIN states ON states.id=cities.state_id""")
    states_db = x.fetchall()
    for a in states_db:
        print(a)
