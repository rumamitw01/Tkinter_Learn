from tkinter import *

def bgUpdate(source):
    red=rSlider.get()
    green=gSlider.get()
    blue=bSlider.get()
    print(f"R={red}, G={green}, B={blue}")
    red=hex(rSlider.get()).replace("0x","")
    green=hex(gSlider.get()).replace("0x","")
    blue=hex(bSlider.get()).replace("0x","")
    if len(red)==1:
        red="0"+red
    if len(green)==1:
        green="0"+green
    if len(blue)==1:
        blue="0"+blue
    myColor="#"+red+green+blue
    root.config(bg=myColor)

root=Tk()
root.title("ch09_04")
root.geometry("360x240")

rSlider=Scale(root,from_=0,to=255,command=bgUpdate)
gSlider=Scale(root,from_=0,to=255,command=bgUpdate)
bSlider=Scale(root,from_=0,to=255,command=bgUpdate)
gSlider.set(125)
rSlider.grid(row=0,column=0)
gSlider.grid(row=0,column=1)
bSlider.grid(row=0,column=2)

root.mainloop()