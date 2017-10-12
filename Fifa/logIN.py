from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class fifa:
    def __init__(self):
        window = Tk()
        window.title("Enter id & Password ")
        l1 = Label(window, text="Username: ").place(x=10,y=10)
        l2 = Label(window, text="Password: ").place(x=10,y=50)
        self.n=StringVar()
        name = Entry(window,textvariable=self.n).place(x=75,y=10)
        self.p=StringVar()
        paswd = Entry(window,textvariable=self.p).place(x=75,y=50)
        log = Button(window, text="Log In",command=self.enter).place(x=50,y=100)
        sign = Button(window, text="Sign Up",command=self.newentry).place(x=100,y=100)
        window.mainloop()

    def enter(self):
        if self.n.get()=='rishav' and self.p.get()=='123':
            tkMessageBox.showinfo("prompt","Welcome Mr "+self.n.get())
            sys.exit(0)
            self.league()
        else:
            tkMessageBox.showinfo("prompt","Unauthorized Entry")



    def newentry(self):
        tkMessageBox.showinfo("prompt","Please Register Here...!")
        self.register()

    def register(self):
        window2 = Tk()
        window2.title("registration form ")
        l1 = Label(window2, text=" Select Username: ").place(x=10,y=10)
        l2 = Label(window2, text="Select Password: ").place(x=10,y=50)
        l2 = Label(window2, text="Confirm Password: ").place(x=10, y=100)
        self.n=StringVar()
        name = Entry(window2,textvariable=self.n).place(x=150,y=10)
        self.p1 = StringVar()
        pass1 = Entry(window2,textvariable=self.p1).place(x=150,y=50)
        self.p2=StringVar()
        pass2 = Entry(window2,textvariable=self.p2).place(x=150,y=100)
        sign = Button(window2, text="Sign Up",command=self.signup).place(x=150,y=200)
        window2.mainloop()

    def signup(self):
        tkMessageBox.showinfo("prompt", "You have been registered successfully " + self.n.get())


    def league(self):
        window = Tk()
        window.title("SELECT YOUR LEAGUE")
        l1 = Label(window, text="SELECT YOUR LEAGUE").place(x=50, y=10)
        b1 = Button(window, text="LA LIGA ", command=self.teamA).place(x=50, y=100)
        b2 = Button(window, text="BARCALAYS ", command=self.teamB).place(x=150, y=100)
        b3 = Button(window, text="BUNDESLIGA ", command=self.teamC).place(x=50, y=150)
        b4 = Button(window, text="SERIE A ", command=self.teamD).place(x=150, y=150)
        window.mainloop()

#team A

    def teamA(self):
        tkMessageBox.showinfo("prompt", "You have selected LaLiga")
        window = Tk()
        window.title("Select your Team")
        rm = Button(window, text="Real Madrid", command=self.openR).place(x=20, y=50)
        bar = Button(window, text="Barcelona", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

#team B

    def teamB(self):
        tkMessageBox.showinfo("prompt", "You have selected EPL")
        window = Tk()
        window.title("Select your Team")
        ar = Button(window, text="Arsenal", command=self.openR).place(x=20, y=50)
        mu = Button(window, text="Manchester United", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

#team C

    def teamC(self):
        tkMessageBox.showinfo("prompt", "You have selected Bundesliga")
        window = Tk()
        window.title("Select your Team")
        dot = Button(window, text="Dortmund", command=self.openR).place(x=20, y=50)
        bm = Button(window, text="Bayren Munich", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

#team D

    def teamD(self):
        tkMessageBox.showinfo("prompt", "You have selected Serie A")
        window = Tk()
        window.title("Select your Team")
        juv = Button(window, text="Juventus", command=self.openR).place(x=20, y=50)
        mil = Button(window, text="A C Milan", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")


fifa()