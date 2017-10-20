from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class reg:
    def __init__(self):
        window = Tk()
        window.title("registration form ")
        l1 = Label(window, text=" Select Username: ").place(x=10,y=10)
        l2 = Label(window, text="Select Password: ").place(x=10,y=50)
        l2 = Label(window, text="Confirm Password: ").place(x=10, y=100)
        self.n=StringVar()
        name = Entry(window,textvariable=self.n).place(x=150,y=10)
        self.p1 = StringVar()
        pass1 = Entry(window,textvariable=self.p1).place(x=150,y=50)
        self.p2=StringVar()
        pass2 = Entry(window,textvariable=self.p2).place(x=150,y=100)
        sign = Button(window, text="Sign Up",command=self.signup).place(x=150,y=200)
        window.mainloop()

    def signup(self):
        tkMessageBox.showinfo("prompt", "You have been registered successfully " + self.n.get())


reg()