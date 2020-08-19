

'''
f
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    messagebox.showinfo(None, 'Lets play a riddle quiz!  Write every answer as lowercase letters. ')
    riddle1 = simpledialog.askstring(None, 'What can fill a room but takes up no space? )')
    riddle2 = simpledialog.askstring(None, 'The more you take, the more you leave behind. What am I?')
    riddle3 = simpledialog.askstring(None, 'When does Christmas come before Thanksgiving?')
    if  riddle1 == 'light':
        messagebox.showinfo(None, 'You are correct!')
        score+=1
    else:
        messagebox.showinfo(None, 'You are wrong! The correct answer was light.')
    if  riddle2 == 'footsteps':
        messagebox.showinfo(None, 'You are correct!')
    else:
        messagebox.showinfo(None, 'You are wrong! The correct answer was footsteps.')


    if riddle3 == 'the dictionary':
        messagebox.showinfo(None, 'You are correct!')
        score+=1
    else:
        messagebox.showinfo(None, 'You are wrong! The correct answer was the dictionary.')
    messagebox.showinfo('You got ' + str(score) + ' out of 3 riddles correct')



