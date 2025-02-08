
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import random

def testfunction():
    var_random = random.randint(1, 3)
    var_label_input = int(entry_input.get())
    if var_random == var_label_input:
        messagebox.showinfo(title="Result", message="It's right!")
    else:
        messagebox.showinfo(title="Result", message="It's false!")

# تابع برای بررسی ورود
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# ایجاد پنجره اصلی با استفاده از تم بوت‌استرپ
root = ttk.Window(themename="darkly")
root.title("Login Form")
root.geometry("500x400")

# تنظیم فونت‌ها
font_title = ("Helvetica", 18, "bold")
font_label = ("Helvetica", 14)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 14, "bold")

# عنوان فرم ورود
label_title = ttk.Label(root, text="Random Game", font=font_title)
label_title.pack(pady=20)

# برچسب و ورودی عدد ورودی
label_input = ttk.Label(root, text="Enter a Number (1-3)", font=font_label)
label_input.pack(pady=10)

entry_input = ttk.Entry(root, font=font_entry)
entry_input.pack(pady=5)

# دکمه ورود
button_login = ttk.Button(root, text="Submit", bootstyle="primary", command=testfunction)
button_login.pack(pady=30)

root.mainloop()
