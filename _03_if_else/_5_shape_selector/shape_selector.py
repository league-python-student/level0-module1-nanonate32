import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    nathan = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(None, "What shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'triangle':
        nathan.forward(100) # draw base
        nathan.left(120)
        nathan.forward(100)
        nathan.left(120)
        nathan.forward(100)
    elif shape == 'square':
        nathan.forward(100)  # Forward turtle by 100 units
        nathan.left(90)  # Turn turtle by 90 degree
        nathan.forward(100)
        nathan.left(90)
        nathan.forward(100)
        nathan.left(90)
        nathan.forward(100)
        nathan.left(90)
    elif shape == 'circle':
        nathan.penup()
        nathan.setpos(0, 0)
        nathan.pendown()
        nathan.circle(100)
    elif shape == 'decagon':
        for i in range(10):
            nathan.forward(100)
            nathan.right(36)


    # Call the turtle .done() method
    turtle.done()
    window.mainloop()