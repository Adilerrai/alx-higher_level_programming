#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ")
    result = cur.fetchall()
    for state in result:
        print(state)
    cur.close()
    db.close()