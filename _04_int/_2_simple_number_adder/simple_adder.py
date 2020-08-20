# Write a Python program that asks the user for two numbers.
from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(None, 'Enter a number.')
    num2 = simpledialog.askinteger(None, 'Enter another number.')
# Then display the sum of the two numbers
num3 = num1 + num2
messagebox.showinfo(None, 'The sum of your two numbers is ' + str(num3) + '.')