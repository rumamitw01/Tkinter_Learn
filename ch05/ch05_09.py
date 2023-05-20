from tkinter import *
def cal():
    out.configure(text="結果是："+str(eval(equ.get())))

root=Tk()
root.title("ch05_09")
label=Label(root,text="請輸入數學表達式：")
label.pack()
equ=Entry(root)
equ.pack(pady=5)
out=Label(root)
out.pack()
btn=Button(root,text="計算",command=cal)
btn.pack(pady=5)

root.mainloop()