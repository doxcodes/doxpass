#password generator program - doxcodes

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwwarning("Warning", "Password length should be at least 4 characters")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number")
        return
    
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_specials = special_var.get()

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_specials:
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = "".join(random.choice(char_pool)for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


#User Interface (Sleek)

root = tk.Tk()
root.title("DoxPass")
root.geometry("450x450")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))

#Main Frame
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

#Title
ttk.Label(frame, text="Secure Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

#Password Lengtgh
ttk.Label(frame, text="Password Length:").pack(anchor="w")
length_var = tk.StringVar(value="12")
ttk.Entry(frame, textvariable=length_var, width=10, font=("Arial", 12)).pack(pady=5)

#Checkbox Frame
checkbox_frame = ttk.LabelFrame(frame, text="Character Options", padding=10)
checkbox_frame.pack(pady=10, fill="x")

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

options = [
    ("Include Uppercase Letters", upper_var),
    ("Include Lowercase Letters", lower_var),
    ("Include Numbers", numbers_var),
    ("Include Special Characters", special_var),
]


for text, var in options:
    ttk.Checkbutton(checkbox_frame, text=text, variable=var).pack(anchor="w")


#Generate Password Button
ttk.Button(frame, text="Generate Password", command=generate_password).pack(pady=10)

#Password Display
password_var = tk.StringVar()
password_entry = ttk.Entry(frame, textvariable=password_var, state='readonly', font=("Arial", 12), width=30)
password_entry.pack(pady=5)

#Clipboard Button
ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)


root.mainloop()
