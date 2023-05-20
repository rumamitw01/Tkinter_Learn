from tkinter import *

def cal():
    monthrate=float(rateVar.get())/(12*100)
    molecules=float(loanVar.get())*monthrate
    denominator=1-(1/(1+monthrate)**(int(yearVar.get())*12))
    monthlypay=int(molecules/denominator)
    monthlypayVar.set(monthlypay)
    totalPay=monthlypay*int(yearVar.get())*12
    totalpayVar.set(totalPay)

window=Tk()
window.title("ch06_08")

Label(window,text="貸款年利率").grid(row=1,column=1,sticky=W)
Label(window,text="貸款年數").grid(row=2,column=1,sticky=W)
Label(window,text="貸款金額").grid(row=3,column=1,sticky=W)
Label(window,text="月付款金額").grid(row=4,column=1,sticky=W)
Label(window,text="總付款金額").grid(row=5,column=1,sticky=W)

rateVar=StringVar()
Entry(window,textvariable=rateVar,justify=RIGHT).grid(row=1,column=2,padx=3)
yearVar=StringVar()
Entry(window,textvariable=yearVar,justify=RIGHT).grid(row=2,column=2,padx=3)
loanVar=StringVar()
Entry(window,textvariable=loanVar,justify=RIGHT).grid(row=3,column=2,padx=3)

monthlypayVar=StringVar()
lblmonthlypay=Label(window,textvariable=monthlypayVar).grid(row=4,column=2,sticky=E,padx=3)
totalpayVar=StringVar()
lbltotalpay=Label(window,textvariable=totalpayVar).grid(row=5,column=2,sticky=E,padx=3)
btn_Cal=Button(window,text="計算貸款金額",command=cal).grid(row=6,column=2,sticky=E,padx=3,pady=3)

window.mainloop()