from tkinter import *
def printSelection():
    print(cities[var.get()])

root=Tk()
root.title("ch07_04")
cities={0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var=IntVar()
var.set(0)
label=Label(root,text="選擇最喜歡的城市",fg="blue",bg="lightyellow",width=30).pack()

for val,city in cities.items():
    Radiobutton(root,text=city,indicatoron=0,width=30,variable=var,value=val,command=printSelection).pack()

root.mainloop()