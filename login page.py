print("hi mahesh")
a = 10
b = 20
sum = a + b

print("Sum:", sum)

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()

