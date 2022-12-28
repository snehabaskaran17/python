from tkinter.ttk import*
from tkinter import*
import mysql.connector as mysql
import random
from datetime import datetime

root= Tk()
root.geometry("1200x650+100+20")
root.title("RESTAURANT MANAGEMENT SYSTEM")

f= Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400,width=300, relief= RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root, bd=5,height=400, width=300, relief=RAISED)

f3 = Frame(root,bd=10,bg='grey', height=400,width=300,relief=GROOVE)
f3.pack(side=BOTTOM)

lbl_info= Label(f, font=('aria', 30, 'bold'),bg='pink',text="XPRESS BRIYANI")
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand         = StringVar()
NammaoorBiryani       = StringVar()
ThalapakattuBiryani = StringVar()
HyderabadiBiryani   = StringVar()
AmburBiryani        = StringVar()
SindhiBiryani       = StringVar()
DumBiryani          = StringVar()
KeemaBiryani        = StringVar()
KolkataBiryani      = StringVar()
MalabarBiryani      = StringVar()
AwadhiBiryani       = StringVar()
Total                = StringVar()
Tax            = StringVar()
cost           = StringVar()
date           = StringVar()
service_charge = StringVar()

lbl_NammaoorBiryani= Label(f1, font=('aria', 20, 'bold'),text="NammaoorBiryani Rs.180")
lbl_NammaoorBiryani.grid(row=1,column=0)
txt_NammaoorBiryani= Entry(f1, font=('ariel', 20, 'bold'),textvariable=NammaoorBiryani)
txt_NammaoorBiryani.grid(row=1,column=1)

lbl_ThalapakattuBiryani= Label(f1, font=('aria', 20, 'bold'),text="ThalapakattuBiryani  Rs.150")
lbl_ThalapakattuBiryani.grid(row=2,column=0)
txt_ThalapakattuBiryani= Entry(f1, font=('ariel', 20, 'bold'),textvariable=ThalapakattuBiryani)
txt_ThalapakattuBiryani.grid(row=2,column=1)

lbl_HyderabadiBiryani= Label(f1, font=('aria', 20, 'bold'),text="HyderabadiBiryani Rs.150")
lbl_HyderabadiBiryani.grid(row=3,column=0)
txt_HyderabadiBiryani= Entry(f1, font=('ariel', 20, 'bold'),textvariable=HyderabadiBiryani)
txt_HyderabadiBiryani.grid(row=3,column=1)

lbl_AmburBiryani = Label(f1, font=('aria', 20, 'bold'),text="AmburBiryani  Rs.200")
lbl_AmburBiryani.grid(row=4,column=0)
txt_AmburBiryani = Entry(f1, font=('ariel', 20, 'bold'),textvariable=AmburBiryani)
txt_AmburBiryani.grid(row=4,column=1)

lbl_SindhiBiryani  = Label(f1, font=('aria', 20, 'bold'),text="SindhiBiryani Rs.200")
lbl_SindhiBiryani.grid(row=5,column=0)
txt_SindhiBiryani = Entry(f1, font=('ariel', 20, 'bold'),textvariable=SindhiBiryani )
txt_SindhiBiryani.grid(row=5,column=1)

lbl_DumBiryani   = Label(f1, font=('aria', 20, 'bold'),text="DumBiryani  Rs.200")
lbl_DumBiryani .grid(row=6,column=0)
txt_DumBiryani = Entry(f1, font=('ariel', 20, 'bold'),textvariable=DumBiryani)
txt_DumBiryani .grid(row=6,column=1)

lbl_KeemaBiryani = Label(f1, font=('aria', 20, 'bold'),text="KeemaBiryani  Rs.150")
lbl_KeemaBiryani.grid(row=7,column=0)
txt_KeemaBiryani = Entry(f1, font=('ariel', 20, 'bold'),textvariable=KeemaBiryani)
txt_KeemaBiryani.grid(row=7,column=1)

lbl_KolkataBiryani = Label(f1, font=('aria', 20, 'bold'),text="KolkataBiryani Rs.160")
lbl_KolkataBiryani.grid(row=8,column=0)
txt_KolkataBiryani = Entry(f1, font=('ariel', 20, 'bold'),textvariable=KolkataBiryani)
txt_KolkataBiryani.grid(row=8,column=1)

lbl_MalabarBiryani  = Label(f1, font=('aria', 20, 'bold'),text="MalabarBiryani Rs.165")
lbl_MalabarBiryani.grid(row=9,column=0)
txt_MalabarBiryani  = Entry(f1, font=('ariel', 20, 'bold'),textvariable=MalabarBiryani)
txt_MalabarBiryani.grid(row=9,column=1)

lbl_AwadhiBiryani  = Label(f1, font=('aria', 20, 'bold'),text="AwadhiBiryani Rs.195")
lbl_AwadhiBiryani.grid(row=10,column=0)
txt_AwadhiBiryani  = Entry(f1, font=('ariel', 20, 'bold'),textvariable=AwadhiBiryani)
txt_AwadhiBiryani.grid(row=10,column=1)



def generate_bill():
    bill_no = str(random.randint(50, 500))
    rand.set(bill_no)
    date.set(localtime)
    try: qn = int(NammaoorBiryani.get())
    except: qn = 0
    try: qt = int(ThalapakattuBiryani.get())
    except: qt = 0
    try: qh = int(HyderabadiBiryani.get())
    except: qh = 0
    try: qa = int(AmburBiryani.get())
    except: qa = 0
    try: qs = int(SindhiBiryani.get())
    except: qs = 0
    try: qd = int(DumBiryani.get())
    except: qd = 0
    try: qk = int(KeemaBiryani.get())
    except: qk =0
    try: qc = int(KolkataBiryani.get())
    except: qc= 0
    try: qm = int(MalabarBiryani.get())
    except: qm= 0
    try: qb = int(AwadhiBiryani.get())
    except: qb= 0
    

    costofNammaoorBiryani = qn * 180 
    costofThalapakattuBiryani = qt * 150
    costofHyderabadiBiryani = qh * 150
    costofAmburBiryani  = qa * 200
    costofSindhiBiryani = qs * 200
    costofDumBiryani    = qd * 200
    costofKeemaBiryani    = qk * 150
    costofKolkataBiryani   = qc * 160
    costofMalabarBiryani    = qm * 165
    costofAwadhiBiryani = qb * 195
    
    f2.pack(side=RIGHT, fill="both", expand=1)
    f2.configure(background="light yellow")

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text="Bill no")
    lbl_bill.grid(row=1,column=0)

    lbl_date = Label(f2, font=('aria', 18, 'bold'), text="Date")
    lbl_date.grid(row=2,column=0)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text="Cost")
    lbl_cost.grid(row=3,column=0)
    
    lbl_service = Label(f2, font=('aria', 18, 'bold'), text="Service charge")
    lbl_service.grid(row=4,column=0)
    
    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text="Tax")
    lbl_tax.grid(row=5,column=0)
    
    lbl_total = Label(f2, font=('aria', 18, 'bold'), text="Total")
    lbl_total.grid(row=6,column=0)
    
    Totalcost= costofNammaoorBiryani  + costofThalapakattuBiryani + costofHyderabadiBiryani  + costofAmburBiryani + costofSindhiBiryani + costofDumBiryani + costofKeemaBiryani + costofKolkataBiryani + costofMalabarBiryani + costofAwadhiBiryani
    costofmeal =  "Rs.", str('%.2f' % Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = "Rs.", str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = "Rs.", str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = "Rs.", str('%.2f' % overall)

    service_charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

txt_bill = Entry(f2, font=('ariel', 18, 'bold'),textvariable=rand)
txt_bill.grid(row=1, column=1)

txt_date = Entry(f2, font=('ariel', 18, 'bold'),textvariable=date)
txt_date.grid(row=2, column=1)

txt_cost = Entry(f2, font=('ariel', 18, 'bold'),textvariable=cost)
txt_cost.grid(row=3, column=1)

txt_service = Entry(f2, font=('ariel', 18, 'bold'),textvariable=service_charge)
txt_service.grid(row=4, column=1)

txt_tax = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Tax)
txt_tax.grid(row=5, column=1)

txt_total = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Total)
txt_total.grid(row=6, column=1)

def qexit():
    root.destroy()
def reset():
    NammaoorBiryani.set('') 
    ThalapakattuBiryani.set('')  
    HyderabadiBiryani.set('') 
    AmburBiryani.set('')      
    SindhiBiryani.set('')  
    DumBiryani.set('')
    KeemaBiryani.set('')
    KolkataBiryani.set('')
    MalabarBiryani.set('')
    AwadhiBiryani.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="CALCULATE BILL",command=generate_bill)
btn_Total.grid(row=13,column=0)

btn_Reset = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="RESET",command=reset)
btn_Reset.grid(row=13,column=1)

btn_Exit = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="EXIT",command=qexit)
btn_Exit.grid(row=13,column=2)

#Calculator

operator=''#7+9
def buttonClick(numbers):#9
    global operator
    operator=operator+numbers
    calculaterField.delete(0,END)
    calculaterField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculaterField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculaterField.delete(0,END)
    calculaterField.insert(0,result)
    operator=''

calculaterField=Entry(f3,font=('arial',16,'bold'),width=32,bd=4)
calculaterField.grid(row=0,column=0,columnspan=4)

button7=Button(f3,text='7',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(f3,text='8',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(f3,text='9',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(f3,text='+',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(f3,text='4',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(f3,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(f3,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(f3,text='-',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(f3,text='1',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(f3,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(f3,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(f3,text='*',font=('arial',16,'bold'),fg='white',bg='light blue',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(f3,text='Ans',font=('arial',16,'bold'),fg='white',bg='black',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(f3,text='Clear',font=('arial',16,'bold'),fg='white',bg='black',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(f3,text='0',font=('arial',16,'bold'),fg='white',bg='black',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(f3,text='/',font=('arial',16,'bold'),fg='white',bg='black',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()







