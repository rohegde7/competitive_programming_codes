import tkinter
from tkinter import*

rr=Tk()
b=Button(rr,justify=LEFT)
p=PhotoImage(file="f.jpg")
b.config(image=p,width="10",height="10")
b.pack(side=LEFT)
rr.mainloop()



