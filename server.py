import random
import socket
import threading
import time
import sqlite3

waiting_list = 0


def login(client_socket):
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
        flag = 0
        # Print Results
        for row in results:
            if username == row[3] and password == row[4]:
                flag = 1
                client_socket.send("yes".encode("utf-8"))
                time.sleep(0.5)
                client_socket.send(str(row[0]).encode("utf-8"))
                print("Log In went successfully")
                return row[0]
        if flag == 0:
            print("Invalid username or password")
            client_socket.send("no".encode("utf-8"))
            return 0
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

def signup(client_socket):
    global id_count
    id_count += 1
    id = id_count
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
        client_socket.send("yes".encode("utf-8"))
        time.sleep(0.5)
        client_socket.send(str(id).encode("utf-8"))
        return id


    except sqlite3.Error as error:
        client_socket.send("You are signed up unsuccessfully".encode("utf-8"))
        print("Failed to insert data into sqlite table", error)
        client_socket.send("no".encode("utf-8"))
        # Rolling back in case of error
        connection.rollback()
    return 0


def handleclient(address, client_socket):
    while True:
        ans = client_socket.recv(1024).decode("utf")
        if ans == "Log":
            id = login(client_socket)
            if id != 0:
                print("The value is an integer.")
                break
            else:
                print("The value is not an integer.")
        if ans == "Signup":
            id = signup(client_socket)
            if id != 0:
                print("The value is an integer.")
                break
            else:
                print("The value is not an integer.")
    print(id)
    while True:
        pass


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
query = "SELECT id FROM Person"
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
all_id = [results[i][0] for i in range(len(results))]
id_count = max(all_id)

while True:
    client_socket, address = s.accept()
    thread1 = threading.Thread(target=handleclient, args = (address, client_socket))
    thread1.start()

