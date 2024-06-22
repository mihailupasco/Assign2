import socket
import time
import tkinter as tk
from tkinter import messagebox

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9000))

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
            age.delete(0, "end")
            age.config(fg='white')

    def on_focusout_name(event):
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

    app.update_idletasks()

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

def destroy():
    for widget in app.winfo_children():
        widget.destroy()


class Game:
    def __init__(self, id):
        self.id = id
        while True:
            aux = s.recv(1024).decode('utf-8')
            if aux[:-4] == str(id):
                self.__target_number = int(aux[-4:])
                break
    def game_itself(self):
        destroy()

        main_frame = tk.Frame(app)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Top center the instruction label
        instruction_label = tk.Label(main_frame, text="Guess the 4 digit number")
        instruction_label.pack(pady=10)

        # Frame to hold the entry boxes and center them horizontally
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack(pady=10)

        entry_width = 5

        def on_entry_num1(event):
            num1.delete(0, "end")  # delete all the text in the entry
            num1.insert(0, '')  # Insert blank for user input
            num1.config(fg='white')

        def on_entry_num2(event):
            num2.delete(0, "end")  # delete all the text in the entry
            num2.insert(0, '')  # Insert blank for user input
            num2.config(fg='white')

        def on_entry_num3(event):
            num3.delete(0, "end")  # delete all the text in the entry
            num3.insert(0, '')  # Insert blank for user input
            num3.config(fg='white')

        def on_entry_num4(event):
            num4.delete(0, "end")  # delete all the text in the entry
            num4.insert(0, '')  # Insert blank for user input
            num4.config(fg='white')

        num1 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num1.insert(index=0, string='1')
        num1.bind('<FocusIn>', on_entry_num1)
        num1.pack(side=tk.LEFT, padx=5, pady=10)

        num2 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num2.insert(index=0, string='2')
        num2.bind('<FocusIn>', on_entry_num2)
        num2.pack(side=tk.LEFT, padx=5, pady=10)

        num3 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num3.insert(index=0, string='3')
        num3.bind('<FocusIn>', on_entry_num3)
        num3.pack(side=tk.LEFT, padx=5, pady=10)

        num4 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num4.insert(index=0, string='4')
        num4.bind('<FocusIn>', on_entry_num4)
        num4.pack(side=tk.LEFT, padx=5, pady=10)

        def guess():
            def fun_game(a, b):
                count = 0
                a = str(a)
                b = str(b)
                for i in range(4):
                    if a[i] == b[i]:
                        count += 1
                return count
            if len(str(num1.get() + num2.get() + num3.get() + num4.get())) != 4:
                messagebox.showinfo("Info", f"The number is not valid, Please enter a 4 digit number")
                return
            s.send(str(str(self.id) + "get_info").encode('utf-8'))
            time.sleep(0.1)
            aux = s.recv(1024).decode('utf-8')
            if aux == str(str(self.id) + "lost"):
                messagebox.showinfo("Info", f"The game is over \n The number was {self.__target_number}, You lost")
                instruction_label = tk.Label(app, text="If you want to play again, restart the game")
                instruction_label.pack()
                destroy()
                return

            result = int(num1.get() + num2.get() + num3.get() + num4.get())
            if result == self.__target_number:
                s.send(str(str(self.id) + "get_info").encode('utf-8'))
                aux = s.recv(1024).decode('utf-8')
                if aux == str(str(self.id) + "lost"):
                    messagebox.showinfo("Info", f"The game is over \n The number was {self.__target_number}, You lost")
                    destroy()
                    instruction_label = tk.Label(app, text="If you want to play again, restart the game")
                    instruction_label.pack()
                    app.update_idletasks()
                    return

                messagebox.showinfo("Info", f"You have won the game !!!")
                s.send(str(str(self.id) + "win").encode('utf-8'))
                destroy()
                instruction_label = tk.Label(app, text="If you want to play again, restart the game")
                instruction_label.pack()
            else:
                s.send(str(str(self.id) + "get_info").encode('utf-8'))
                aux = s.recv(1024).decode('utf-8')
                if aux == str(str(self.id) + "lost"):
                    messagebox.showinfo("Info", f"The game is over \n The number was {self.__target_number}, You lost")
                    destroy()
                    instruction_label = tk.Label(app, text="If you want to play again, restart the game")
                    instruction_label.pack()
                    app.update_idletasks()
                    return
                messagebox.showinfo("Info", f"You got {fun_game(result, self.__target_number)} digits right Try again")
        submit_button = tk.Button(main_frame, text="Submit", command=guess)
        submit_button.pack(pady=10)
        app.update_idletasks()


def handle_client(id):
    destroy()
    print("You are in the game", id)
    def play_game():
        s.send(str(str(id)+"Play").encode('utf-8'))
        destroy()
        app.update_idletasks()
        while True:
            aux = s.recv(1024).decode('utf-8')
            if aux == "The game has started":
                print("The game has started")
                break
        destroy()

        main_frame = tk.Frame(app)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Top center the instruction label
        instruction_label = tk.Label(main_frame, text="Choose a 4 digit number for your opponent to guess")
        instruction_label.pack(pady=10)

        # Frame to hold the entry boxes and center them horizontally
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack(pady=10)

        entry_width = 5

        def on_entry_num1(event):
            num1.delete(0, "end")  # delete all the text in the entry
            num1.insert(0, '')  # Insert blank for user input
            num1.config(fg='white')

        def on_entry_num2(event):
            num2.delete(0, "end")  # delete all the text in the entry
            num2.insert(0, '')  # Insert blank for user input
            num2.config(fg='white')

        def on_entry_num3(event):
            num3.delete(0, "end")  # delete all the text in the entry
            num3.insert(0, '')  # Insert blank for user input
            num3.config(fg='white')

        def on_entry_num4(event):
            num4.delete(0, "end")  # delete all the text in the entry
            num4.insert(0, '')  # Insert blank for user input
            num4.config(fg='white')

        num1 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num1.insert(index=0, string='1')
        num1.bind('<FocusIn>', on_entry_num1)
        num1.pack(side=tk.LEFT, padx=5, pady=10)

        num2 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num2.insert(index=0, string='2')
        num2.bind('<FocusIn>', on_entry_num2)
        num2.pack(side=tk.LEFT, padx=5, pady=10)

        num3 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num3.insert(index=0, string='3')
        num3.bind('<FocusIn>', on_entry_num3)
        num3.pack(side=tk.LEFT, padx=5, pady=10)

        num4 = tk.Entry(entry_frame, fg='grey', width=entry_width)
        num4.insert(index=0, string='4')
        num4.bind('<FocusIn>', on_entry_num4)
        num4.pack(side=tk.LEFT, padx=5, pady=10)

        def send():
            result = str(id) + num1.get()+num2.get()+num3.get()+num4.get()
            s.send(result.encode('utf-8'))
            user = Game(id)
            user.game_itself()


        submit_button = tk.Button(main_frame, text="Submit",command=send)
        submit_button.pack(pady=10)
        app.update_idletasks()

    instruction_label = tk.Label(app, text="Press play and wait for someone to join")
    instruction_label.pack()
    play_button = tk.Button(app, text="Play", command=play_game)
    play_button.pack()


app.mainloop()

a = input()

s.close()

