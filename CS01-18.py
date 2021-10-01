from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My name is ",fg="#A155B9",font=20).grid(row=0,column=0)
myText = Label(text="Nongnaphasorn ",fg="#F765A3",font=20).grid(row=1,column=1)
myText = Label(text="Chumchoosri ",fg="#FFA4B6",font=20).grid(row=2,column=2)
root.mainloop()