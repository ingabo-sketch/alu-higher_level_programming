#!/usr/bin/python3
"""List states whose name matches the given argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = database.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
