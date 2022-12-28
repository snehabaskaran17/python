from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import mysql.connector as mysql

root=Tk()
root.title('Billing Management system')
root.geometry('1280x720')
bg_color='#209290'




#====================Button===============
Bread=IntVar()
Wine=IntVar()
Rice=IntVar()
Milk=IntVar()
Total_cost=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()


#=========================funcions=====================
def Total():
    if Bread.get()==0 and Wine.get()==0 and Rice.get()==0 and Milk.get()==0 and Total_cost.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        w=Wine.get()
        r=Rice.get()
        m=Milk.get()
        tc=Total_cost.get()

        t=int(b*30+w*500+r*1500+m*40)
        cb.set('Rs'+str(round(b*30,2)))
        cw.set('Rs'+str(round(w*500,2)))
        cr.set('Rs'+str(round(r*1500,2)))
        cm.set('Rs'+str(round(m*40,2)))
        total_cost.set('Rs'+str(round(t,2)))
        
                
def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Item\tNumber of Items \tCost of Items')
    textarea.insert(END,f'\n\nBread\t\t{Bread.get()}\t {cb.get()}')
    textarea.insert(END,f'\n\nWine\t\t{Wine.get()}\t {cw.get()}')
    textarea.insert(END,f'\n\nRice\t\t{Rice.get()}\t {cr.get()}')
    textarea.insert(END,f'\n\nMilk\t\t{Milk.get()}\t {cm.get()}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\nTotal Price\t\t{Total_cost.get()}\t{total_cost.get()}')
    textarea.insert(END,'\n\n================================')


def extra_root():
    new_root = Toplevel(root)
    new_root.title("Billing Management System")
    new_root.geometry("450x450")
    Label(new_root,text='Billing').pack()
    Label(new_root, text=b_txt.get()).pack()
    Label(new_root, text=w_txt.get()).pack()
    Label(new_root, text=r_txt.get()).pack()
    Label(new_root, text=m_txt.get()).pack()
    
    new_root.mainloop()
    
def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Wine.set(0)
    Rice.set(0)
    Milk.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cm.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()


    
                    



title=Label(root,text='Billing Management system',relief=GROOVE,)
title.pack(fill=X)

#=================Product details=================
F1=LabelFrame(root,text='Product Details',relief=RIDGE)
F1.place(x=5,y=90,width=800,height=500)

#================Heading==========================
itm=Label(F1,text='Items')
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items')
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='Cost of Items')
cost.grid(row=0,column=2,padx=20,pady=15)

#=================Product=======================
bread=Label(F1,text='Bread')
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',textvariable=Bread)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',textvariable=cb)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

wine=Label(F1,text='Wine')
wine.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',textvariable=Wine)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',textvariable=cw)
cw_txt.grid(row=2,column=2,padx=20,pady=15)

rice=Label(F1,text='Rice')
rice.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',textvariable=Rice)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',textvariable=cr)
cr_txt.grid(row=3,column=2,padx=20,pady=15)

milk=Label(F1,text='Milk')
milk.grid(row=4,column=0,padx=20,pady=15)
m_txt=Entry(F1,font='arial 15 bold',textvariable=Milk)
m_txt.grid(row=4,column=1,padx=20,pady=15)
cm_txt=Entry(F1,font='arial 15 bold',textvariable=cm)
cm_txt.grid(row=4,column=2,padx=20,pady=15)

    

#====================bill area========================
F2=Frame(root,relief=GROOVE)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Receipt').pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 bold',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)


#=======================Button=====================
F3=Frame(root,relief=GROOVE)
F3.place(x=5,y=590,width=1270,height=120)


btn1=Button(F3,text='Total',command=Total)
btn1.grid(row=0,column=0,padx=30,pady=10)

btn2=Button(F3,text='Receipt',command=receipt)
btn2.grid(row=0,column=1,padx=30,pady=10)

btn3=Button(F3,text='Print',command=extra_root)
btn3.grid(row=0,column=2,padx=30,pady=10)

btn4=Button(F3,text='Reset',command=reset)
btn4.grid(row=0,column=3,padx=30,pady=10)

btn5=Button(F3,text='Exit',command=exit)
btn5.grid(row=0,column=4,padx=30,pady=10)



def save_data():
    bread = b_txt.get()
    wine = w_txt.get()
    rice = r_txt.get()
    milk = m_txt.get()


    con = mysql.connect(host="localhost",user="root",password="",database="billing")
    cursor = con.cursor()
    cursor.execute("insert into billing_table values('"+ bread +"','"+ wine +"','"+ rice +"','" + milk +"')")
    cursor.execute("commit")

    con.close()
   
Button(root,text='Save Details', command=save_data).pack()
root.mainloop()


                   
    
    



















root.mainloop()
