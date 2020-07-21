##Label Frames:

import tkinter as tk
from tkinter import ttk

win=tk.Tk()

##labelframes
labelframe1=ttk.LabelFrame(win,text="Registration Form")
labelframe1.grid(row=0,column=0,padx=10,pady=10)

labelframe2=ttk.LabelFrame(win,text="Contact Form")
labelframe2.grid(row=0,column=1,padx=10,pady=10)


##creating widgets in labelframes1
label1=ttk.Label(labelframe1,text="Enter Name:")
label1.grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)

label2=ttk.Label(labelframe1,text="Enter Age:")
label2.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)


nameentry=ttk.Entry(labelframe1,width=18)
nameentry.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

ageentry=ttk.Entry(labelframe1,width=18)
ageentry.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)




##creating widgets in labelframes1
label11=ttk.Label(labelframe2,text="Enter Name:")
label11.grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)

label21=ttk.Label(labelframe2,text="Enter Age:")
label21.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)


nameentry1=ttk.Entry(labelframe2,width=18)
nameentry1.grid(row=0,column=1,sticky=tk.W,padx=5,pady=5)

ageentry1=ttk.Entry(labelframe2,width=18)
ageentry1.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)



win.mainloop()
