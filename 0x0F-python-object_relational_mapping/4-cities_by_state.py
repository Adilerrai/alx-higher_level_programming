#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

        # Get MySQL connection parameters from command line arguments
        username, password, database = sys.argv[1:]

        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object using the cursor() method
        cursor = db.cursor()

        # Execute a single query to retrieve the required data
        cursor.execute(
            """
                SELECT cities.id, cities.name, states.na
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """
        )

        # Fetch all the rows using the fetchall() method
        rows = cursor.fetchall()

        # Display the results as specified
        for row in rows:
            print(row)

            # Close the cursor and database connection
            cursor.close()
            db.close()
