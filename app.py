from tkinter import *

import cryptage
import pyperclip as pc


def crypt():
    cryptInputText.delete("1.0", "end-1c")
    cryptInputText.insert(INSERT,list(cryptage.cryptLong(UncryptInputText.get("1.0", "end-1c"),cryptage.cle)))

def unCrypt():
    UncryptInputText.delete("1.0", "end-1c")
    UncryptInputText.insert(INSERT,cryptage.unCryptLong(stringToList(cryptInputText.get("1.0", "end-1c")),cryptage.cle))

def copyCrypt():
    pc.copy(cryptInputText.get("1.0", "end-1c"))
def copyUncrypt():
    pc.copy(str(UncryptInputText.get("1.0", "end-1c")))

def stringToList(mot):

    mot = mot.split('} {')

    b = []
    for k in mot:
        b.append(k.replace('{',''))
    mot = []
    for k in b:
        mot.append(k.replace('}',''))
    for k in range(len(mot)):
        if mot[k] == '':
            del mot[k]
    b = []
    for k in range(len(mot)):
        mot[k] = mot[k].split(' ')
        for i in range(len(mot[k])):
            mot[k][i] = int(mot[k][i])
    return mot

gui = Tk()
gui.title("crypt App")
gui.geometry('520x250')


gui.grid_columnconfigure(0, weight=1)
gui.grid_columnconfigure(1, weight=1)

#crypt:

#label
label=Label(gui,text="Enter your sentence to crypt")

label.grid(column=0,row=0, padx=0, pady=0)

#input
UncryptInputText = Text(gui,bd=1,width=22,height=10)
UncryptInputText.grid(column=0,row=1, padx=0, pady=0)

#copy button
copyButton = Button(gui, text="copy", bd='2', command=copyUncrypt)
copyButton.grid(column=0,row=2, padx=0, pady=0)

#button
submit1 = Button(gui, text="→", bd='2', command=crypt)
submit1.place(x=250,y=75)

#uncrypt

#label
label=Label(gui,bd='2',text="Enter your sentence to Uncrypt")

label.grid(column=1,row=0, padx=0, pady=0)

#input
cryptInputText = Text(gui,bd=1,width=22,height=10)
cryptInputText.grid(column=1,row=1, padx=0, pady=0)

#copy button
copyButton2 = Button(gui, text="copy", bd='2', command=copyCrypt)
copyButton2.grid(column=1,row=2, padx=0, pady=0)

#button
submit2 = Button(gui, text="←", bd='2', command=unCrypt)
submit2.place(x=250,y=100)

gui.mainloop()