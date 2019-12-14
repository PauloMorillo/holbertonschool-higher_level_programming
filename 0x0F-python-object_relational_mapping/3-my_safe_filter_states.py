#!/usr/bin/python3
"""This Module prints all of a database"""
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
    cur.execute("SELECT * FROM states WHERE name = BINARY %s ORDER BY id",
                [sys.argv[4]])
    rows = cur.fetchall()
    for _row in rows:
        print(_row)
if __name__ == '__main__':
    main()
