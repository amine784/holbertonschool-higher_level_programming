#!/usr/bin/python3
''' script tha list all states'''

import sys
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    query = "SELECT * FROM states WHERE name = '{}'".format(
        sys.argv[4])
    cur = data.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    data.close()
