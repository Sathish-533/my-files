import tkinter as tk
import mysql.connector
from tkinter import messagebox

def submitact():
    user = Username.get()
    passw = password.get()
    if user and passw:
        logintodb(user, passw)
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password.")

def logintodb(user, passw):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="your_password", db="College")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM STUDENT WHERE username = %s AND password = %s", (user, passw))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Login Success", "Welcome, {}".format(user))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        db.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

root = tk.Tk()
root.geometry("300x200")
root.title("DBMS Login Page")

tk.Label(root, text="Username:").pack(pady=5)
Username = tk.Entry(root, width=35)
Username.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password = tk.Entry(root, width=35, show="*")
password.pack(pady=5)

submitbtn = tk.Button(root, text="Login", bg='blue', command=submitact)
submitbtn.pack(pady=20)

root.mainloop()
