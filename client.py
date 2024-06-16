import socket
import time
import tkinter as tk
from tkinter import messagebox

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))



username = str()
password = str()

app = tk.Tk()
app.geometry("400x500")
app.title("Guess the Code Game")

# Label for instructions


instruction_label = tk.Label(app, text="Log in")
instruction_label.pack()



def on_entry_click_username(event):
    """Function to be called when the entry box is clicked"""
    if username.get() == 'Username':
        username.delete(0, "end")  # delete all the text in the entry
        username.insert(0, '')  # Insert blank for user input
        username.config(fg='white')

def on_entry_click_password(event):
    if password_label.get() == 'Password':
        password_label.delete(0, "end")  # Delete all the text in the entry
        password_label.config(show='*', fg='white')

def on_focusout_username(event):
    """Function to be called when the entry box loses focus"""
    if username.get() == '':
        username.insert(0, 'Username')
        username.config(fg='grey')

def on_focusout_password(event):
    if password_label.get() == '':
        password_label.insert(0, 'Password')
        password_label.config(fg='grey')

username = tk.Entry(app, fg='grey')
username.insert(0, 'Username')
username.bind('<FocusIn>', on_entry_click_username)  # Bind on_entry_click to the focus in event
username.bind('<FocusOut>', on_focusout_username)  # Bind on_focusout to the focus out event
username.pack()

password_label = tk.Entry(app, fg='grey')
password_label.insert(0, 'Password')
password_label.bind('<FocusIn>', on_entry_click_password)  # Bind on_entry_click to the focus in event
password_label.bind('<FocusOut>', on_focusout_password)  # Bind on_focusout to the focus out event
password_label.pack()

def log_in():
    global username
    global password
    while True:
        userName = username.get()
        passWord = password_label.get()
        s.send("Log".encode('utf-8'))
        time.sleep(0.5)
        s.send(userName.encode('utf-8'))
        time.sleep(0.5)
        s.send(passWord.encode('utf-8'))

        print(userName, passWord)

        fromServer = s.recv(1024).decode('utf-8')
        if fromServer == "yes":
            messagebox.showinfo("Info", f"You are logged in successfully")
            time.sleep(0.5)
            handle_client(int(s.recv(1024).decode('utf-8')))
            break
        else:
            messagebox.showinfo("Info", f"You are logged in unsuccessfully, try again")
            break


# Button to submit the code
submit_button = tk.Button(app, text="Log In", command=log_in)
submit_button.pack()



def sign_up():

    for widget in app.winfo_children():
        widget.destroy()

    sign_label = tk.Label(app, text="Sign Up")
    sign_label.pack()

    def on_entry_click_username(event):
        """Function to be called when the entry box is clicked"""
        if username.get() == 'Username':
            username.delete(0, "end")  # delete all the text in the entry
            username.insert(0, '')  # Insert blank for user input
            username.config(fg='white')

    def on_entry_click_password(event):
        if password_label.get() == 'Password':
            password_label.delete(0, "end")  # Delete all the text in the entry
            password_label.config(show='*', fg='white')

    def on_focusout_username(event):
        """Function to be called when the entry box loses focus"""
        if username.get() == '':
            username.insert(0, 'Username')
            username.config(fg='grey')

    def on_focusout_password(event):
        if password_label.get() == '':
            password_label.insert(0, 'Password')
            password_label.config(fg='grey')

    def on_entry_click_name(event):
        """Function to be called when the entry box is clicked"""
        if name.get() == 'Name':
            name.delete(0, "end")  # delete all the text in the entry
            name.insert(0, '')  # Insert blank for user input
            name.config(fg='white')

    def on_entry_click_age(event):
        if age.get() == 'Age':
            age.delete(0, "end")  # Delete all the text in the entry
            age.config(fg='white')

    def on_focusout_name(event):
        """Function to be called when the entry box loses focus"""
        if name.get() == '':
            name.insert(0, 'Name')
            name.config(fg='grey')

    def on_focusout_age(event):
        if age.get() == '':
            age.insert(0, 'Age')
            age.config(fg='grey')

    name = tk.Entry(app, fg='grey')
    name.insert(0, 'Name')
    name.bind('<FocusIn>', on_entry_click_name)  # Bind on_entry_click to the focus in event
    name.bind('<FocusOut>', on_focusout_name)  # Bind on_focusout to the focus out event
    name.pack()

    age = tk.Entry(app, fg='grey')
    age.insert(0, 'Age')
    age.bind('<FocusIn>', on_entry_click_age)  # Bind on_entry_click to the focus in event
    age.bind('<FocusOut>', on_focusout_age)  # Bind on_focusout to the focus out event
    age.pack()

    username = tk.Entry(app, fg='grey')
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_entry_click_username)  # Bind on_entry_click to the focus in event
    username.bind('<FocusOut>', on_focusout_username)  # Bind on_focusout to the focus out event
    username.pack()

    password_label = tk.Entry(app, fg='grey')
    password_label.insert(0, 'Password')
    password_label.bind('<FocusIn>', on_entry_click_password)  # Bind on_entry_click to the focus in event
    password_label.bind('<FocusOut>', on_focusout_password)  # Bind on_focusout to the focus out event
    password_label.pack()

    def send_data():
        age1 = age.get()
        try:
            age_vallue = int(age1)

        except:
            messagebox.showinfo("Info", f"The age is not valid")
            return
        else:
            s.send("Signup".encode('utf-8'))
            time.sleep(0.5)
            s.send(name.get().encode('utf-8'))
            time.sleep(0.5)
            s.send(str(age_vallue).encode('utf-8'))
            time.sleep(0.5)
            s.send(username.get().encode('utf-8'))
            time.sleep(0.5)
            s.send(password_label.get().encode('utf-8'))

        FromServer = s.recv(1024).decode('utf-8')
        if FromServer == "yes":
            messagebox.showinfo("Info", f"You are signed up successfully")
            handle_client(int(s.recv(1024).decode('utf-8')))
        else:
            messagebox.showinfo("Info", f"You are signed up unsuccessfully, try again")


    send_data = tk.Button(app, text="Sign Up", command=send_data)
    send_data.pack()


sign_up_button = tk.Button(app, text="Sign Up", command=sign_up)
sign_up_button.pack()


def handle_client(id):
    for widget in app.winfo_children():
        widget.destroy()
    print("You are in the game")
    print(id)





app.mainloop()



a = input()

s.close()

