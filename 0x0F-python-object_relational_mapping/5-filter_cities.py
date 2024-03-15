#!/usr/bin/python3
""" lists all cities of the state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db_list = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])
    x = db_list.cursor()
    x.execute("""SELECT cities.id, cities.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE states.name LIKE BINARY %(state_name)s \
              ORDER BY cities.id ASC""", {'state_name': argv[4]})
    cities_db = x.fetchall()
    city_list = list(a[0] for a in cities_db)
    print(*city_list, sep=", ")
    x.close()
    db_list.close()
