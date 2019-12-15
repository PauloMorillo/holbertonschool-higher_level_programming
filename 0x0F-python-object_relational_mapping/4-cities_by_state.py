#!/usr/bin/python3
"""This Module prints all of a relational databases"""
import sys
import MySQLdb


def main():
    """main function"""
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities"
                " RIGHT JOIN states ON cities.state_id = states.id"
                " ORDER BY cities.id")
    rows = cur.fetchall()
    for _row in rows:
        print(_row)
if __name__ == '__main__':
    main()
