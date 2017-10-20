import tkinter
from tkinter import*

class transfer:
    def __init__(self):
        window = Tk()
        window.title("transfer/loan")
        self.v1 = IntVar()
        l1 = Radiobutton(window, text="Transfer",variable=self.v1,value=1,command=self.select).place(x=10,y=10)
        l2 = Radiobutton(window, text="Loan", variable=self.v1,value=2, command=self.select).place(x=100,y=10)
        l3=Label(window,text="Enter Your Amount in $ :: ").place(x=10,y=50)
        self.price=IntVar()
        amount=Entry(window,textvariable=self.price).place(x=10,y=50)
        btn=Button(window, text="Submit",command=self.submit).place(x=125,y=100)
        window.mainloop()

    def select(self):
        if self.v1.get() == 1 :
            print("You have selected to transfer the player :")
        else:
            print("You have selected to send on loan ! ")

    def submit(self):
        print("Your Amount has been submitted $",+self.price.get())

transfer()