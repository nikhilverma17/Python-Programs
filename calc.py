##label 1
##label 2
##
##add sub div mul
##
##result in entry box
import tkinter as tk
from tkinter import ttk
from tkinter import *
win=tk.Tk()
win.title("Calculator")
win.geometry('600x400+500+200')
win.configure(background="blue")
##win.wm_attributes('-transparentcolor','black')
##
##filename = PhotoImage(file = "pic.gif")
##background_label = Label(win, image=filename)
##background_label.place(x=0, y=0, relwidth=1, relheight=1)

##input
label1=ttk.Label(win,text="First Number:")
label1.grid(row=0,column=0,padx=5,pady=5)
num1=tk.IntVar()
number1=ttk.Entry(win,textvariable=num1)
number1.grid(row=0,column=1,padx=5,pady=5)

label2=ttk.Label(win,text="Second Number:")
label2.grid(row=1,column=0,padx=5,pady=5)
num2=tk.IntVar()
number2=ttk.Entry(win,textvariable=num2)
number2.grid(row=1,column=1,padx=5,pady=5)

label3=ttk.Label(win,text="Answer:")
label3.grid(row=3,column=0,padx=5,pady=5)


ans=tk.IntVar()
Answer=ttk.Entry(win,textvariable=ans)
Answer.grid(row=3,column=1,padx=5,pady=5)

def add():
    a=num1.get()
    b=num2.get()
    ans.set(a+b)

##addbtn
addbtn=ttk.Button(win,text="Add", command=add)
addbtn.grid(row=2,column=0,padx=5,pady=5)


def sub():
    a=num1.get()
    b=num2.get()
    ans.set(a-b)

##subbtn
subbtn=ttk.Button(win,text="Sub", command=sub)
subbtn.grid(row=2,column=1,padx=5,pady=5)



def mul():
    a=num1.get()
    b=num2.get()
    ans.set(a*b)

##mulbtn
mulbtn=ttk.Button(win,text="Mul", command=mul)
mulbtn.grid(row=2,column=2,padx=5,pady=5)



def div():
    a=num1.get()
    b=num2.get()
    ans.set(a/b)

##divbtn
divbtn=ttk.Button(win,text="Divide", command=div)
divbtn.grid(row=2,column=3,padx=5,pady=5)


win.mainloop()
