#!/usr/bin/python3
""" List all states from hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY state.id ")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()