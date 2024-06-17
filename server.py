import random
import socket
import threading
import time
import sqlite3



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
    game(id, address, client_socket)


waiting_list = 0
rooms = []

def game(id, address, client_socket):
    global waiting_list
    our_players_and_numbers = [[0, 0], [0, 0]]
    # In this 2 while loops we connect the players to the game
    while True:
        a = client_socket.recv(1024).decode("utf-8")
        if a[-4:] == "Play":
            if a[:-4] == str(id):
                if waiting_list %2 == 0:
                    waiting_list += 1
                    rooms.append([id])
                    print("player ", id, " is waiting")
                    break
                else:
                    waiting_list += 1
                    rooms[-1].append(id)
                    print("player ", id, " entered the game", rooms[-1])
                    break
    our_room_index = len(rooms) - 1

    while True:
        if len(rooms[-1]) == 2:
            our_players_and_numbers[0][0] = rooms[-1][0]
            our_players_and_numbers[1][0] = rooms[-1][1]
            rooms[-1] = our_players_and_numbers
            print("The game has started", rooms[our_room_index])
            client_socket.send("The game has started".encode("utf-8"))
            break
    while True:
        response = client_socket.recv(1024).decode("utf-8")
        if int(response[:-4]) == id:
            if rooms[our_room_index][0][0][0] == id:
                rooms[our_room_index][0][0][1] = int(response[-4:])
            else:
                rooms[our_room_index][1][0][1] = int(response[-4:])
            break
    print(rooms[our_room_index])
    for i in range(10):
        time.sleep(0.3)
        client_socket.send(str(str(rooms[our_room_index][0][0][0]) + str(rooms[our_room_index][1][0][1])).encode("utf-8"))
        time.sleep(0.3)
        client_socket.send(str(str(rooms[our_room_index][1][0][0]) + str(rooms[our_room_index][0][0][1])).encode("utf-8"))





s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 9000))
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

