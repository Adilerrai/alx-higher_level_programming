#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='Localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
