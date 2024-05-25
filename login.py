import sqlite3

def read_data():
    # Connect to an SQLite database
    connection = sqlite3.connect('data.db')

    # Create a cursor object using the cursor() method
    cursor = connection.cursor()

    # SQL query to retrieve data
    query = "SELECT * FROM Person"

    try:
        # Execute the SQL command
        cursor.execute(query)

        # Fetch all rows from the last executed statement
        results = cursor.fetchall()

        # Print Results
        for row in results:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Username:", row[3])
            print("Password:", row[4])

    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

    finally:
        # Close the database connection
        if connection:
            connection.close()
            print("SQLite connection is closed")

# Call the function to read data
read_data()
