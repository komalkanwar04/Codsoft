import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("450x250")
        self.root.configure(bg="#282c34")
        self.root.resizable(True, True)

        # Configure grid layout for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure([0,1,2,3], weight=1)

        # Label for instruction
        self.label = tk.Label(root, text="Enter desired password length:", font=("Arial", 14), bg="#282c34", fg="#61dafb")
        self.label.grid(row=0, column=0, columnspan=2, pady=(20,10), sticky="ew")

        # Entry for password length
        self.length_var = tk.StringVar()
        self.length_entry = tk.Entry(root, textvariable=self.length_var, font=("Arial", 14), width=10, justify='center')
        self.length_entry.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew", padx=50)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 14), bg="#61dafb", fg="#282c34", activebackground="#21a1f1", activeforeground="white")
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew", padx=100)

        # Label to display generated password
        self.password_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#98c379", bg="#282c34", wraplength=400)
        self.password_label.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew", padx=20)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive integer for password length.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
