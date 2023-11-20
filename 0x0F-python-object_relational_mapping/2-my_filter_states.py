#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    pattern = sys.argv[4]
    query =  "SELECT * FROM states WHERE name REGEXP CONCAT('^', %s) COLLATE utf8mb4_bin ORDER BY id ASC;"
    cur.execute(query, (pattern,))

    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
