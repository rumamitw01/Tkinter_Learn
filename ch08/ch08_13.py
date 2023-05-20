from tkinter import *

def color_Radiobutton():
    if var.get()=="blue_color":
        lbl["fg"]="blue"
    elif var.get()=="green_color":
        lbl["fg"]="green"
    elif var.get()=="red_color":
        lbl["fg"]="red"

def new_text_Btn():
    lbl["text"]=msg.get()

window=Tk()
window.title("ch08_13")

frame1=Frame(window)
frame1.pack()
lbl=Label(frame1,text="Python GUI是有趣的")
lbl.pack()

frame2=Frame(window)
frame2.pack()
label=Label(frame2,text="請輸入文字：")
msg=StringVar()
entry=Entry(frame2,textvariable=msg)
change_Text=Button(frame2,text="更改文字",command=new_text_Btn)
var=StringVar()
var.set(1)
rb_blue=Radiobutton(frame2,text="淺藍",bg="lightblue",variable=var,value="blue_color",command=color_Radiobutton)
rb_green=Radiobutton(frame2,text="淺綠",bg="lightgreen",variable=var,value="green_color",command=color_Radiobutton)
rb_red=Radiobutton(frame2,text="紅色",bg="red",variable=var,value="red_color",command=color_Radiobutton)

label.grid(row=1,column=1)
entry.grid(row=1,column=2)
change_Text.grid(row=1,column=3)
rb_blue.grid(row=2,column=1)
rb_green.grid(row=2,column=2)
rb_red.grid(row=2,column=3)

window.mainloop()