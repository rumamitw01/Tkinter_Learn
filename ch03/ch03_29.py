from tkinter import *

window=Tk()
window.title("ch03_29")
lab1=Label(window,text="標籤1",relief="raised")
lab2=Label(window,text="標籤2",relief="raised")
lab4=Label(window,text="標籤4",relief="raised")
lab5=Label(window,text="標籤5",relief="raised")
lab8=Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab8.grid(row=1,column=3)

window.mainloop()