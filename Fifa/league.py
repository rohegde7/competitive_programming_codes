from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class league:
    def __init__(self):
        window = Tk()
        window.title("SELECT YOUR LEAGUE")
        l1 = Label(window, text="SELECT YOUR LEAGUE").place(x=50,y=10)
        b1 = Button(window, text="LA LIGA ",command=self.teamA).place(x=50,y=100)
        b2 = Button(window, text="BARCALAYS ",command=self.teamB).place(x=150,y=100)
        b3 = Button(window, text="BUNDESLIGA ",command=self.teamC).place(x=50,y=150)
        b4 = Button(window, text="SERIE A ",command=self.teamD).place(x=150,y=150)
        window.mainloop()

    def teamA(self):
        tkMessageBox.showinfo("prompt", "You have selected LaLiga")

    def teamB(self):
        tkMessageBox.showinfo("prompt", "You have selected EPL")

    def teamC(self):
        tkMessageBox.showinfo("prompt", "You have selected Bundesliga")

    def teamD(self):
        tkMessageBox.showinfo("prompt", "You have selected Serie A")

    def __init__(self):
        window = Tk()
        window.title("SELECT YOUR LEAGUE")
        l1 = Label(window, text="SELECT YOUR LEAGUE").place(x=50, y=10)
        b1 = Button(window, text="LA LIGA ", command=self.teamA).place(x=50, y=100)
        b2 = Button(window, text="BARCALAYS ", command=self.teamB).place(x=150, y=100)
        b3 = Button(window, text="BUNDESLIGA ", command=self.teamC).place(x=50, y=150)
        b4 = Button(window, text="SERIE A ", command=self.teamD).place(x=150, y=150)
        window.mainloop()

    def teamA(self):
        tkMessageBox.showinfo("prompt", "You have selected LaLiga")

    def teamB(self):
        tkMessageBox.showinfo("prompt", "You have selected EPL")

    def teamC(self):
        tkMessageBox.showinfo("prompt", "You have selected Bundesliga")

    def teamD(self):
        tkMessageBox.showinfo("prompt", "You have selected Serie A")


league()