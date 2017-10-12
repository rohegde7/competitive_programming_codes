from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class teamA:
    def __init__(self):
        window = Tk()
        window.title("Select your Team")
        rm = Button(window, text="Real Madrid", command=self.openR).place(x=20, y=50)
        bar = Button(window, text="Barcelona", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
teamA()