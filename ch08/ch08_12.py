from tkinter import *

def click_Radiobutton():
    print(("淺藍色" if v1.get()==1 else "淺綠色")+"設定")

def click_bold_box():
    print("粗體鈕"+("設定" if v2.get()==1 else "取消設定"))

def click_italic_box():
    print("斜體鈕"+("設定" if v3.get()==1 else "取消設定"))

def get_Name():
    print("姓名："+name.get())

window=Tk()
window.title("ch08_12")

frame1=Frame(window)
frame1.pack()

v1=IntVar()
v1.set(1)
rb_blue=Radiobutton(frame1,text="淺藍",bg="lightblue",variable=v1,value=1,command=click_Radiobutton)
rb_green=Radiobutton(frame1,text="淺綠",bg="lightgreen",variable=v1,value=2,command=click_Radiobutton)

v2=IntVar()
cbtBold=Checkbutton(frame1,text="粗體",variable=v2,command=click_bold_box)

v3=IntVar()
cbtItalic=Checkbutton(frame1,text="斜體",variable=v3,command=click_italic_box)

rb_blue.grid(row=1,column=1)
rb_green.grid(row=1,column=2)
cbtBold.grid(row=2,column=1)
cbtItalic.grid(row=2,column=2)

frame2=Frame(window)
frame2.pack()
label=Label(frame2,text="請輸入名字：")
name=StringVar()
name_Entry=Entry(frame2,textvariable=name)
name_Btn=Button(frame2,text="執行",command=get_Name)

label.grid(row=1,column=1)
name_Entry.grid(row=1,column=2)
name_Btn.grid(row=1,column=3)

lbl=Label(window,text="控件組合應用")
lbl.pack()

window.mainloop()