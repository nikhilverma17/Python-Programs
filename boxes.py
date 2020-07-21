import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title("Boxes")
win.geometry("300x200+500+200")

labelframe=ttk.Labelframe(win,text="Contact Details")
labelframe.grid(row=0,column=0,padx=10,pady=10)

label1=ttk.Label(labelframe,text="Enter your name")
label1.grid(row=0,column=0,padx=10,pady=10)

label2=ttk.Label(labelframe,text="Enter your age")
label2.grid(row=0,column=1,padx=10,pady=10)

namevar=tk.StringVar()
name=ttk.Entry(labelframe,width=20,textvariable=namevar)
name.grid(row=1,column=0,padx=10,pady=10)

agevar=tk.StringVar()
age=ttk.Entry(labelframe,width=20,textvariable=agevar)
age.grid(row=1,column=1,padx=10,pady=10)

def submit():
    n=namevar.get()
    a=agevar.get()
    if n=='' or a == '':
        m_box.showerror('Error','Plz fill both name and age')
    else:
        try:
            a=int(a)
        except ValueError:
            m_box.showwarning('Error','Only digits are allowed in age field')
        else:
            if a<18:
                m_box.showwarning('Warning','You are not 18, visit this content on your own risk.')
            else:
                m_box.showinfo('Info','Information')
            print(f'{n} {a}')



submitbtn=ttk.Button(labelframe,text="Submit",command=submit)
submitbtn.grid(row=2,columnspan=2,padx=10,pady=10)


win.mainloop()
