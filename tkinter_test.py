import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Tkinter Test Window")

    # Create a label
    label = ttk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=10)

    # Create a button
    def on_button_click():
        label.config(text="Button Clicked!")

    button = ttk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()