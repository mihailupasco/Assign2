import tkinter as tk
from tkinter import messagebox

def creting_the_app():
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

    username = tk.Entry(app,fg='grey')
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_entry_click_username)  # Bind on_entry_click to the focus in event
    username.bind('<FocusOut>', on_focusout_username)  # Bind on_focusout to the focus out event
    username.pack()

    password_label = tk.Entry(app,fg='grey')
    password_label.insert(0, 'Password')
    password_label.bind('<FocusIn>', on_entry_click_password)  # Bind on_entry_click to the focus in event
    password_label.bind('<FocusOut>', on_focusout_password)  # Bind on_focusout to the focus out event
    password_label.pack()

    def submit_code():
        userName = username.get()
        password = password_label.get()
        print(userName, password)
        # You would add your networking code here to send the code to the server
        messagebox.showinfo("Info", f"Your user name is {userName} and your password is {password}")


    # Button to submit the code
    submit_button = tk.Button(app, text="Submit Code", command=submit_code)
    submit_button.pack()


    # Run the application
    app.mainloop()
