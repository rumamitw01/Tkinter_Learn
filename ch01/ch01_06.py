from tkinter import *
root=Tk()
screenwidth,screenheight=root.winfo_screenwidth(),root.winfo_screenheight()
w,h=300,160
x,y=(screenwidth-w)/2,(screenheight-h)/2
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
root.mainloop()