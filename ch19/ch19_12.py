from tkinter import *

tk=Tk()
canvas=Canvas(tk,width=640,height=480)
canvas.pack()
canvas.create_text(200,50,text="Ming-Chi Institute of Technology")
canvas.create_text(200,80,text="Ming-Chi Institute of Technology",fill="blue")
canvas.create_text(300,120,text="Ming-Chi Institute of Technology",fill="blue",font=("Old English Text MT",20))
canvas.create_text(300,160,text="Ming-Chi Institute of Technology",fill="blue",font=("Arial",20))
canvas.create_text(300,200,text="明志科技大學",fill="blue",font=("Times",20))

tk.mainloop()