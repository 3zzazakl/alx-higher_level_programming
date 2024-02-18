#!/usr/bin/python3
"""Connecting to mysql database and listing all states
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """_summary_
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s ORDER \
                   BY id ASC".format(sys.argv[4]), (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
