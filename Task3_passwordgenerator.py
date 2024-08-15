import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x150")

        self.length_label = tk.Label(self.window, text="Enter password length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.window)
        self.length_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self.window, text="Generated Password:")
        self.password_label.pack()

        self.password_text = tk.Text(self.window, height=1, width=30)
        self.password_text.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8 characters.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(tk.END, password)
        except ValueError:
            messagebox.showerror("Error", "Invalid password length. Please enter a number.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()