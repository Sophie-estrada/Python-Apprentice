"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

# Import the required modules
from tkinter import * 
# Create a window object
window = Tk()
window.title("Infuriating Calculator")
# Hide the window, hint: use the withdraw method
window.withdraw()
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
# Ask the user for the first number   
first_number = simpledialog.askfloat("First Number", "Enter the first number:")
# Ask the user for the second number
second_number = simpledialog.askfloat("Second Number", "Enter the second number:")
# Ask the user for the math operation
operation = simpledialog.askstring("Math Operation", "Enter the math operation (add, subtract, multiply, divide):")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "add":
    result = first_number + second_number
    messagebox.showinfo("Result", f"The result of {first_number} + {second_number} is: {result}")
elif operation == "subtract":
    result = first_number - second_number
    messagebox.showinfo("Result", f"The result of {first_number} - {second_number} is: {result}")
elif operation == "multiply":
    result = first_number * second_number
    messagebox.showinfo("Result", f"The result of {first_number} * {second_number} is: {result}")
elif operation == "divide":    
    if second_number != 0:
        result = first_number / second_number
        messagebox.showinfo("Result", f"The result of {first_number} / {second_number} is: {result}")
    else:
        messagebox.showerror("Error", "Cannot divide by zero.")
else:
    messagebox.showerror("Error", "Unknown operation. Please enter add, subtract, multiply, or divide.")
    