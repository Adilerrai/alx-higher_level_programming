#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (sys.argv[4],))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
