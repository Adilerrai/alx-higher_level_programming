#!/usr/bin/python3
"""Script that list all state """
import MySQLdb
import sys


def list_stat(username, password, database):
    """lists all states from the database hbtn_0e_0_usa.
    Ags:
    username: mysql username
    password: mysql password
    database: mysql database
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    connect = MySQLdb.connect(host="127.0.0.1", port=3306, user=username,
                              passwd=password, db=database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connect.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_stat(username, password, database)
