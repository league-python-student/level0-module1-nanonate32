from tkinter import Tk, messagebox, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    secretMessage = simpledialog.askstring(None, "What is the secret message?")
    password = simpledialog.askstring(None, "What is the password for the secret message?")
    if password == 'yeet':
        messagebox.showinfo(None, secretMessage)
    else:
        messagebox.showinfo(None, "INTRUDER!!!")

