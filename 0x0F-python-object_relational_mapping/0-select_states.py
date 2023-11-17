#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(user="root", password="Viveraja123@",
                     database="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("SELECT * FROM states ")
# Fetch all results
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i])

# Close the connection
db.close()
