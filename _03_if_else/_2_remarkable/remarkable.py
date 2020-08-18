from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, "What is your name?")
    if name == "leonard":
        messagebox.showinfo(None, "You are remarkable because you are very proficient at designing web sites.")
    if name == "ruhi":
        messagebox.showinfo(None, "You are remarkable because you know how to ask for help when you are having problevems.")
    if name == "dave":
        messagebox.showinfo(None, "You are remarkable because you know how to code python and are a very succesful programmer.")