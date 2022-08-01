from tkinter import *

import cryptage
import pyperclip as pc


def crypt():
    pc.copy(cryptage.cryptLong(UncryptInputText.get(),cryptage.cle))
def unCrypt():
    pc.copy(cryptage.unCryptLong(cryptInputText.get(),cryptage.cle))

gui = Tk()
gui.title("crypt App")
gui.geometry('250x200')

#crypt:

#label
label=Label(gui,text="Enter your sentence to crypt")

label.pack()

#input
UncryptInputText = Entry(gui,bd=1)
UncryptInputText.pack()

#button
submit1 = Button(gui, text="copy result", bd='2', command=crypt)
submit1.pack()

#uncrypt

#label
label=Label(gui,bd='2',text="Enter your sentence to Uncrypt")

label.pack()

#input
cryptInputText = Entry(gui,bd=1)
cryptInputText.pack()

#button
submit2 = Button(gui, text="copy result", bd='2', command=unCrypt)
submit2.pack()

gui.mainloop()