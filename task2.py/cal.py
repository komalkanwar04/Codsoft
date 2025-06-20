import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        # Remove fixed size to allow resizing
        # self.root.geometry("320x400")
        self.root.minsize(320, 400)
        self.root.resizable(True, True)

        self.expression = ""

        # Display frame
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
        self.display.pack(fill='both', ipadx=8, ipady=15, padx=10, pady=10, expand=True)

        # Buttons frame
        btns_frame = tk.Frame(root)
        btns_frame.pack(fill='both', expand=True)

        # Configure grid weights for responsiveness
        for i in range(5):
            btns_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btns_frame.columnconfigure(j, weight=1)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text in {'+', '-', '*', '/', '='}:
                bg_color = '#ADD8E6'  # Light blue for operation and equals buttons
                fg_color = 'black'
            elif text == 'C':
                bg_color = '#FF6347'  # Tomato red for clear button
                fg_color = 'white'
            else:
                bg_color = '#D3D3D3'  # Light gray for digit buttons
                fg_color = 'black'

            button = tk.Button(btns_frame, text=text, font=("Arial", 18), 
                               bg=bg_color, fg=fg_color,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.display_var.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
                self.display_var.set("")
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
