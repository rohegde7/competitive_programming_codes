from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class teamA:
    def __init__(self):
        window = Tk()
        window.title("Select your Team")
        ar = Button(window, text="Arsenal", command=self.openR).place(x=20, y=50)
        mu = Button(window, text="Manchester United", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
teamA()