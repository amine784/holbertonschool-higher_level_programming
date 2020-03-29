#!/usr/bin/python3
''' script tha list all states'''

import sys
import MySQLdb

if __name__ == "__main__":
    data = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = data.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states\
    ON state_id=states.id WHERE states.name=%s"
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    delim = ", "
    print(delim.join(lc[0] for lc in query_rows))
    cur.close()
    data.close()
