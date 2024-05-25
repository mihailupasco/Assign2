import random
import socket
import threading
import time
import sqlite3


waiting_list = 0

def handleclient(address, client_socket):
    print("A client from address", address, "Just connected")
    login(address, client_socket)
def login(address, client_socket):
    client_socket.sendall("Are you already registered ?\n".encode("utf-8"))
    log_info = client_socket.recv(1024).decode("utf-8")
    if log_info == "Y":
        username = client_socket.recv(1024).decode("utf-8")
        time.sleep(0.5)
        password = client_socket.recv(1024).decode("utf-8")
        query = "SELECT * FROM Person"
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        try:
            # Execute the SQL command
            cursor.execute(query)

            # Fetch all rows from the last executed statement
            results = cursor.fetchall()
            print(results)
            # Print Results
            for row in results:
                if username == row[3]:
                    print("The user name exists")
                if password == row[4]:
                    print("The password is correct")
        except sqlite3.Error as error:
            print("Error while connecting to SQLite", error)
    elif log_info == "N":
        id = 2
        name = client_socket.recv(1024).decode("utf-8")
        time.sleep(0.5)
        age = int(client_socket.recv(1024).decode("utf-8"))
        time.sleep(0.5)
        username = client_socket.recv(1024).decode("utf-8")
        time.sleep(0.5)
        password = client_socket.recv(1024).decode("utf-8")
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # Preparing SQL queries to INSERT a new record into the database
        insert_query = """
            INSERT INTO Person (id, name, age, username, password)
            VALUES (?, ?, ?, ?, ?);
            """
        data_tuple = (id, name, age, username, password)
        try:
            # Executing the SQL command
            cursor.execute(insert_query, data_tuple)

            # Commit your changes in the database
            connection.commit()
            print("Data inserted successfully")

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            # Rolling back in case of error
            connection.rollback()




def game(address, client_socket):
    print("A client from address", address, "Just connected")
    # asking for the name

    client_socket.sendall("Do you want to play a game? (Y/N)\n".encode("utf-8"))
    answer = client_socket.recv(1024).decode("utf-8")
    if answer == "Y":
        print("we enter the loop")
        flag = 0
        while waiting_list < 2:
            if flag == 0:
                client_socket.sendall("We are waiting for another player to join, currently 1/2".encode("utf-8"))
                flag = 1

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 8000))
s.listen()
while True:
    client_socket, address = s.accept()
    thread1 = threading.Thread(target=handleclient, args = (address, client_socket))
    thread1.start()

