from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

password = "tocnaLozinka"

def buttonForPasswordPressed ():
    given_pass = entryPass.get()
    if (given_pass != password):
        messagebox.showwarning("Wrong Password")
    else:
        root.deiconify()
        pasScreen.destroy()
        print ("Correct. Continue working on this!") 




root=Tk()
root.title("Python Flower Pots")
root.geometry ("700x500+100+100")
root.iconbitmap ("ikonica.ico")
root.withdraw()

pasScreen = Toplevel()
pasScreen.title ("Python Flower Pots")
pasScreen.geometry ("500x400+200+200")
pasScreen.iconbitmap ("ikonica.ico")
global entryPass
Label (pasScreen, text = "Please enter your password.").grid(column=1,row=0)
entryPass = Entry(pasScreen, width = 22)
entryPass.grid(column=1,row=1)
Button (pasScreen, text = "OK", command = buttonForPasswordPressed).grid (column = 2, row = 1)

root.mainloop()


