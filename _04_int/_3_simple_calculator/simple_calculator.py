# Write a Python program that asks the user for two numbers.
from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(None, 'Enter a number.')
    num2 = simpledialog.askinteger(None, 'Enter another number.')

# Then ask the user if the would like to add, subtract, multiply, or divide.
    operation = simpledialog.askstring(None, 'Would you like to add, multiply, subtract or divide?')
# Use if-else statements to provide the desired math operation on the numbers and display the result.
    if operation == 'add':
       num3 = num1 + num2
       messagebox.showinfo(None, 'The sum of your two numbers is ' + str(num3) + '.')
    elif operation == 'subtract':
        num3 = num1 - num2
        messagebox.showinfo(None, 'The difference of your two numbers is ' + str(num3) + '.')
    elif operation == 'multiply':
        num3 = num1 * num2
        messagebox.showinfo(None, 'The product of your two numbers is ' + str(num3) + '.')
    elif operation == 'divide':
        num3 = num1 / num2
        messagebox.showinfo(None, 'The quotient of your two numbers is ' + str(num3) + '.')