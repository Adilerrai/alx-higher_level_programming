#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER  BY  id ")
    # Fetch all results
    results = cursor.fetchall()
    for i in range(len(results)):
        print(results[i])

    # Close the connection
    cursor.close()
    db.close()
