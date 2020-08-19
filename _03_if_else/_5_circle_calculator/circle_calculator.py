from tkinter import Tk, messagebox, simpledialog
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

# Write a Python program that asks the user for the radius of a circle.
    radius = simpledialog.askinteger(None, 'What is the radius of the circle?')
    area = math.pi * radius * radius
    circumference = math.pi * 2 * radius
# Next, ask the user if they would like to calculate the area or circumference of a circle.
    calculation = simpledialog.askstring(None, 'Would you like to calculate the area or the circumference of the circle?')
# If they choose area, display the area of the circle using the radius.
    if calculation == 'area':
        messagebox.showinfo(None, 'The area of the circle is ' + str(area))

# Otherwise, display the circumference of the circle using the radius.
    else:
        messagebox.showinfo(None, 'The cirumference of the circle is ' + str(circumference))


#Area = πr^2
#Circumference = 2πr 