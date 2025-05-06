import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    chars = ""

    if use_letters:
        chars += string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Require at least letters or digits
    if not (use_letters or use_digits):
        messagebox.showerror("Error", "You must include letters and/or digits!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

def toggle_letters():
    if not letters_var.get() and not digits_var.get():
        letters_var.set(True)
    
    # Disable "Include Uppercase" if letters are unchecked
    if not letters_var.get():
        upper_check.config(state="disabled")
    else:
        upper_check.config(state="normal")

def toggle_digits():
    if not digits_var.get() and not letters_var.get():
        digits_var.set(True)

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#2c2c2c")

# Variables
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Widgets
tk.Label(root, text="Password Length:", bg="#2c2c2c", fg="white").pack(pady=5)
tk.Spinbox(root, from_=4, to=64, textvariable=length_var, width=5).pack()

# Letter and Digit Checkboxes with toggle functionality
tk.Checkbutton(root, text="Include Letters (a-z)", variable=letters_var, bg="#2c2c2c", fg="white", selectcolor="#444", command=toggle_letters).pack(anchor="w", padx=20)
upper_check = tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var, bg="#2c2c2c", fg="white", selectcolor="#444")
upper_check.pack(anchor="w", padx=40)

tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var, bg="#2c2c2c", fg="white", selectcolor="#444", command=toggle_digits).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols (!@#)", variable=symbols_var, bg="#2c2c2c", fg="white", selectcolor="#444").pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#444", fg="white").pack(pady=10)

tk.Entry(root, textvariable=result_var, width=40, justify="center").pack(pady=10)

root.mainloop()
