#!/usr/bin/python3
"""Script that lists all a given state from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":

    # Getconnection parameters and state name from command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using the cursor() method
    cursor = db.cursor()

    # Execute a single query to retrieve the required data
    cursor.execute(
        """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """,
        (state_name,)
    )

    # Fetch the result using the fetchone() method
    result = cursor.fetchone()[0]

    # Display the result as specified
    if result:
        print(result)
    else:
        print("Not found")

        # Close the cursor and database connection
    cursor.close()
    db.close()
