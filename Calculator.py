import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        window_width = 250
        window_height = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.expression_entry = tk.Entry(self.main_frame, font=("Arial", 14), bd=2, relief="flat", justify="right")
        self.expression_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            btn = tk.Button(self.main_frame, text=button, font=("Arial", 14), bd=2, relief="raised", command=lambda b=button: self.on_button_click(b))
            if button in ['+', '-', '*', '/', 'C','=']:
                btn.config(bg="Pink", fg="red")
            else:
                btn.config(bg="Pink")
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col > 3:
                col = 0
                row += 1
    def on_button_click(self, button):
        current_expression = self.expression_entry.get()
        if button == 'C':
            self.expression_entry.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(current_expression)
                self.expression_entry.delete(0, tk.END)
                self.expression_entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {str(e)}")
        else:
            self.expression_entry.insert(tk.END, button)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
