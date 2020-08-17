from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring("", "When is your birthday? Respond using the format of month/day")
    if birthday == "8/17":
        messagebox.showinfo(title = None, message = "Happy birthday to you!")
    else:
        messagebox.showinfo(title = None, message = "Have a very merry unbirthday!")

    window.mainloop()