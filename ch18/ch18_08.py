from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

root=Tk()
root.title("ch18_08")

Style().configure("Treeview",rowheight=35)

info=["鳳凰新聞App可以獲得中國各地最新消息","瑞士國家鐵路App提供全瑞士火車時刻表","可口可樂App是一個娛樂的軟體"]

tree=Treeview(root,columns=("說明"))
tree.heading("#0",text="App")
tree.heading("#1",text="功能說明")
tree.column("#1",width=300)

img1=Image.open("news.jpg")
imgObj1=ImageTk.PhotoImage(img1)
tree.insert("",index=END,text="鳳凰新聞",image=imgObj1,values=info[0])

img2=Image.open("sbb.jpg")
imgObj2=ImageTk.PhotoImage(img2)
tree.insert("",index=END,text="瑞士鐵路",image=imgObj2,values=info[1])

img3=Image.open("coca.jpg")
imgObj3=ImageTk.PhotoImage(img3)
tree.insert("",index=END,text="可口可樂",image=imgObj3,values=info[2])
tree.pack()

root.mainloop()