import tkinter as tk
import secrets
import string


def generate_password():
    password_length = int(length_entry.get())
    if password_length < 5:
        password_label.config(text="Password length should be at least 5 characters",fg="red")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters)for _ in range(password_length))
    password_label.config(text="Generated Password:" + password,fg="green")

window = tk.Tk()
window.title("Random Password Generator")

length_label = tk.Label(window,text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate  Password",command=generate_password)
generate_button.pack()

password_label = tk.Label(window,text="")
password_label.pack()

window.mainloop()