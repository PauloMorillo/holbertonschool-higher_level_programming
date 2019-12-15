#!/usr/bin/python3
"""This Module prints cities of state in a relational databases"""
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
    cur.execute("SELECT cities.name FROM cities"
                " INNER JOIN states ON cities.state_id = states.id"
                " WHERE states.name = %s  ORDER BY cities.id", [sys.argv[4]])
    rows = cur.fetchall()
    a = 0
    for _row in rows:
        if a != 0:
            print(", ", end="")
        a = a + 1
        print("{}".format(_row[0]), end="")
    print("")
if __name__ == '__main__':
    main()
