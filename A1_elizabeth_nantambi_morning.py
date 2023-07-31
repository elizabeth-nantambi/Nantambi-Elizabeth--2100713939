#INHERITANCE 
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name + " is eating")
    
class Dog(Animal):
    def bark(self):
        print(self.name + " is barking")

class Cat(Animal):
    def meow(self):
        print(self.name + " is meowing")

#creating objects
cat= Cat("Chloe")
cat.eat()
cat.meow()


# Exercise

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Example usage
rectangle = Rectangle(4, 5)
print("Area of rectangle:", rectangle.area())

circle = Circle(3)
print("Area of circle:", circle.area())

    

print("\n\n")
print("================================")
#ASSIGNMENT
import tkinter as tk

def generate_receipt():
    # Retrieve input values from the entry fields
    customer_name = entry_name.get()
    item_name = entry_item.get()
    item_price = entry_price.get()

    # Calculate the total price
    total_price = float(item_price) * float(entry_quantity.get())

    # Clear the receipt text area
    #receipt_text.delete("1.0", tk.END)

    # Generate the receipt
    receipt_text.insert(tk.END, "Customer Name: {}\n".format(customer_name))
    receipt_text.insert(tk.END, "Item: {}\n".format(item_name))
    receipt_text.insert(tk.END, "Price: ${}\n".format(item_price))
    receipt_text.insert(tk.END, "Quantity: {}\n".format(entry_quantity.get()))
    receipt_text.insert(tk.END, "------------------------\n")
    receipt_text.insert(tk.END, "Total Price: ${:.2f}".format(total_price))

# Create the main window
window = tk.Tk()
window.title("Nantambi Elizabeth Receipt Generator")

# Create labels and entry fields for input
label_name = tk.Label(window, text="Customer Name:")
label_name.grid(row=0, column=0, sticky=tk.W)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

label_item = tk.Label(window, text="Item:")
label_item.grid(row=1, column=0, sticky=tk.W)
entry_item = tk.Entry(window)
entry_item.grid(row=1, column=1)

label_price = tk.Label(window, text="Price:")
label_price.grid(row=2, column=0, sticky=tk.W)
entry_price = tk.Entry(window)
entry_price.grid(row=2, column=1)

label_quantity = tk.Label(window, text="Quantity:")
label_quantity.grid(row=3, column=0, sticky=tk.W)
entry_quantity = tk.Entry(window)
entry_quantity.grid(row=3, column=1)

# Create a button to generate the receipt
button_generate = tk.Button(window, text="Produce Receipt", command=generate_receipt)
button_generate.grid(row=4, column=0, columnspan=2)

# Create a text area to display the receipt
receipt_text = tk.Text(window, width=40, height=10)
receipt_text.grid(row=5, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()
