##GUI
import tkinter as tk
import os
from tkinter import ttk
from csv import DictWriter
win=tk.Tk()
win.title("Data Entry")
win.geometry('600x450')
win.configure(background='goldenrod')
win.resizable(0,0)
##win.iconbitmap('') give icon path(flaticon.com)
##creating widgets:- ##labels,entryboxes,comboboxes,radiobuttons,checkboxes,buttons##ttk
##layout managers ##pack, grid, place



##labels
namelabel=ttk.Label(win,text="Enter your name:",font=['Helvatica',12,'bold'])
namelabel.grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)
namelabel.configure(foreground='red',background='black')

agelabel=ttk.Label(win,text="Enter your age:",font=['Helvatica',12,'bold'])
agelabel.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)
agelabel.configure(foreground='red')

citylabel=ttk.Label(win,text="Select your city:",font=['Helvatica',12,'bold'])
citylabel.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)
citylabel.configure(foreground='red',background='goldenrod')

#entryboxes
namevar=tk.StringVar()
nameentry=ttk.Entry(win,width=18,textvariable=namevar)
nameentry.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)
agevar=tk.StringVar()
ageentry=ttk.Entry(win,width=18,textvariable=agevar)
ageentry.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

##combo boxes
cityvar=tk.StringVar()
citycombo=ttk.Combobox(win,width=12,state='readonly',textvariable=cityvar)
citycombo['values']=('---Select---','Kanpur','Lucknow','Others')
citycombo.current(0)
citycombo.grid(row=2,column=1)

##Radiobutton
gendervar=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='Male',value='Male',variable=gendervar)
radiobtn1.grid(row=3,column=0)
radiobtn2=ttk.Radiobutton(win,text='Female',value='Female',variable=gendervar)
radiobtn2.grid(row=3,column=1)

##checkbutton
checkvar1=tk.IntVar()
checkbtn1=ttk.Checkbutton(win,text="Do you want to subscribe?",variable=checkvar1)
checkbtn1.grid(row=4,columnspan=2)

##button function

def submit():
    name=namevar.get()
    age=agevar.get()
    city=cityvar.get()
    gender=gendervar.get()

    if checkvar1.get()==0:
        subscribe='No'
    else:
        subscribe='Yes'

    print (f"Name: {name} Age: {age} City: {city} Gender: {gender} Subscription: {subscribe}")

    with open('file.csv','a',newline="") as f:
        dwrite=DictWriter(f,fieldnames=['Name','Age','City','Gender','Subscription'])
        if os.stat('file.csv').st_size==0:
            dwrite.writeheader()

        dwrite.writerow({
            'Name':name,
            'Age':age,
            'City':city,
            'Gender':gender,
            'Subscription':subscribe
            })
        


def cancel():
    win.destroy()

##buttons
submitbtn=ttk.Button(win,text="Submit", command=submit)
submitbtn.grid(row=5,columnspan=2,padx=5,pady=5)
cancelbtn=ttk.Button(win,text="Cancel", command=cancel)
cancelbtn.grid(row=6,columnspan=2,padx=5,pady=5)
##resetbtn=ttk.Button(win,text="Reset", command=win.reset)
##resetbtn.grid(row=7,columnspan=2,padx=5,pady=5)

















win.mainloop()
