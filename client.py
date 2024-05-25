import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))

FromServer = s.recv(1024)

log = input(FromServer.decode('utf-8'))
s.send(log.encode('utf-8'))
if log == "Y":
    user = input("Enter your username: ")
    s.send(user.encode('utf-8'))
    password = input("Enter your password: ")
    s.send(password.encode('utf-8'))
elif log == "N":
    name = input("Enter your name: ")
    s.send(name.encode('utf-8'))
    age = input("Enter your age: ")
    s.send(age.encode('utf-8'))
    username = input("Enter your username: ")
    s.send(username.encode('utf-8'))
    password = input("Enter your password: ")
    s.send(password.encode('utf-8'))




print(FromServer.decode('utf-8'))
a = input()

s.close()

