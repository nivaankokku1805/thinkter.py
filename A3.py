from tkinter import *

root = Tk()
root.title("Getting started with widgets")
root.geometry('400x300')

lbl = Label( text="Full name ", fg="white", bg="#3895D3",)
lbl2 = Label( text="Email Id ", fg="white", bg="#3895D3",)
lbl3 = Label( text="Enter Password", fg="white", bg="#3895D3",)

name_entry = Entry()
email_entry = Entry()
password_entry = Entry(show="*")

def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nCongragratulations for your new account!" 
    textbox.insert(END, greet)
    textbox.insert(END, message)
     
textbox = Text(bg="#BEBEBE",fg="black", )
btn = Button(text="Create account",command=display, )

lbl.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
password_entry.pack()
btn.pack()
textbox.pack()
mainloop()
    