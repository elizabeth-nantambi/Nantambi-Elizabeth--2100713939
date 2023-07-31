
import tkinter as tk
from tkinter import ttk

def add():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result = number1 + number2
    result_label.config(text="Result: " + str(result))

def subtract():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result = number1 - number2
    result_label.config(text="Result: " + str(result))

def divide():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    if number2 != 0:
        result = number1 / number2
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Error: Division by zero")

def multiply():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result = number1 * number2
    result_label.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Nantambi Elizabeth Simple Calculator")  # Set the title for the window

# Create label and entry field for the first number
label1 = ttk.Label(window, text="First Number:")
label1.pack()

entry1 = ttk.Entry(window)
entry1.pack()

# Create label and entry field for the second number
label2 = ttk.Label(window, text="Second Number:")
label2.pack()

entry2 = ttk.Entry(window)
entry2.pack()

# Create buttons for each operation
add_button = ttk.Button(window, text="+", command=add)
add_button.pack()

subtract_button = ttk.Button(window, text="-", command=subtract)
subtract_button.pack()

divide_button = ttk.Button(window, text="/", command=divide)
divide_button.pack()

multiply_button = ttk.Button(window, text="*", command=multiply)
multiply_button.pack()

# Create label for displaying the result
result_label = ttk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
