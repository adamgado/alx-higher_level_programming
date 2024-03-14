#!/usr/bin/python3
""" lists all cities of the state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db_list = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])
    x = db_list.cursor()
    x.execute("""SELECT cities.name FROM
              cities INNER JOIN states ON states.id=cities.state_id
              WHERE states.name=%s""", (sys.argv[4],))
    cities_db = x.fetchall()
    temp = list(a[0] for a in cities_db)
    print(*temp, sep=", ")
