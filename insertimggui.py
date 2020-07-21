##inserting image
##it only reads .gif and .png format img files

import tkinter as tk
from tkinter import ttk

win=tk.Tk()

pic=tk.PhotoImage(file='code3.png')

imglabel=ttk.Label(win,image=pic,text="Hello World",compound=tk.LEFT,font=['Helvatica',40,'bold'])
imglabel.configure(foreground="red")
##imglabel.grid(row=0,column=0)
imglabel.pack(pady=30)
win.mainloop()
