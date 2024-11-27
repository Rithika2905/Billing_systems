from tkinter import *
from tkinter import messagebox
import random
windows = Tk()


billnumber= random.randint(500,1000)
#Function
def total():
    global t,kh,fe,bw,tf,oe,ge,dc,pe,db,horrorprice,comedyprice,fictionprice
    kh=int(Killer_house_entry.get())*10
    fe=int(Feast_entry.get())*20
    bw=int(Bog_wife_entry.get())*30

    tf=int(Tina_fey_entry.get())*10
    oe=int(Omens_entry.get())*20
    ge=int(Guncle_entry.get())*30

    dc=int(Davince_code_entry.get())*10
    pe=int(Powerless_entry.get())*20
    db=int(Dan_brown_entry.get())*30

    horrorprice = kh+fe+bw
    Horrorp_entry.delete(0,END)
    Horrorp_entry.insert(0,horrorprice)
    comedyprice = tf+oe+ge
    Comedyp_entry.delete(0,END)
    Comedyp_entry.insert(0,comedyprice)
    fictionprice = dc+pe+db
    Fictionp_entry.delete(0,END)
    Fictionp_entry.insert(0,fictionprice)
    
    t=horrorprice+comedyprice+fictionprice

def billing():
    if Name_entry.get()=="" or Number_entry.get()=="":
        messagebox.showerror('Oops','Buyer deails missing')
    elif Horrorp_entry.get()=="" or Comedyp_entry.get()=="" or Fictionp_entry.get()=="":
        messagebox.showerror('Oops','Buyer deails missing')
    else:
        text.delete(1.0,END)
        text.insert(END,"\n\t\t\tWELCOME\n")
        text.insert(END,f'\nBill Number : {billnumber}\n')
        text.insert(END,f'Name : {Name_entry.get()}\n')
        text.insert(END,f'Number : {Number_entry.get()}\n')
        text.insert(END,"\n******************************************************\n")

        text.insert(END,f'Book name\t\tQuantity\t\tPrice\n')
        if Killer_house_entry.get() != '0':
            text.insert(END,f'\nKiller house\t\t{Killer_house_entry.get()}\t\t{kh}')
        if Feast_entry.get() != '0':
            text.insert(END,f'\nFeast\t\t{Feast_entry.get()}\t\t{fe}')
        if Bog_wife_entry.get() != '0':
            text.insert(END,f'\nBog wife\t\t{Bog_wife_entry.get()}\t\t{bw}')
        if Tina_fey_entry.get() != '0':
            text.insert(END,f'\nTina fey\t\t{Tina_fey_entry.get()}\t\t{tf}')
        if Omens_entry.get() != '0':
            text.insert(END,f'\nOmens\t\t{Omens_entry.get()}\t\t{oe}')
        if Guncle_entry.get() != '0':
            text.insert(END,f'\nGuncle\t\t{Guncle_entry.get()}\t\t{ge}')
        if Davince_code_entry.get() != '0':
            text.insert(END,f'\nDavince\t\t{Davince_code_entry.get()}\t\t{dc}')
        if Powerless_entry.get() != '0':
            text.insert(END,f'\nPowerless\t\t{Powerless_entry.get()}\t\t{pe}')
        if Dan_brown_entry.get() != '0':
            text.insert(END,f'\nDan brown\t\t{Dan_brown_entry.get()}\t\t{db}')

        text.insert(END,"\n\n******************************************************\n")

        if Horrorp_entry.get() != '0':
            text.insert(END, f'\nHorror price\t\t{horrorprice}')
        if Comedyp_entry.get() != '0':
            text.insert(END, f'\nHorror price\t\t{comedyprice}')
        if Fictionp_entry.get() != '0':
            text.insert(END, f'\nHorror price\t\t{fictionprice}')
        text.insert(END,f'\n\nTotal Amount \t\t{t}')

        save()

def save():
    global billnumber
    res= messagebox.askyesno('Save','Confirm to save file')
    if res:
        content = text.get(1.0,END)
        file = open(f'bills/ {billnumber}.txt','w')
        file.write(content)
        file.close()
        messagebox.showinfo('Ohoo',f'{billnumber} saved successfully !!')
        billnumber = random.randint(500,1000)

import os

def submitnum():
    for i in os.listdir('/bills'):
        if i.split('.')[0] == Bill_num_entry.get():
            f = open(f'bills/{i}' , 'r')
            text.delete(1.0, END)
            for data in f:
                text.insert(END , data)
            f.close()
        
        else:
            messagebox.showerror('Oops', 'File not exists')

#GUI
windows.geometry('1300x750')
windows.title("Tkinter")
windows.iconbitmap('icon.ico')
label= Label(windows, text="Billing corner", font=("times new roman", 20, 'bold'), height=2,background="#bfbfbf", foreground="black")
label.pack(fill=X)

frame= LabelFrame(windows, text="Customer info", font=("times new roman", 18, 'bold'), background="#d9d9d9")
frame.pack( fill=X, pady=10)

Name = Label(frame, text="Name", font=("times new roman", 16), background="#d9d9d9")
Name.grid(row=0 , column=0, padx=30, pady = 2)
Name_entry= Entry(frame, font=("times new roman", 16))
Name_entry.grid(row=0 , column=1, padx=8)
Number = Label(frame,text="Number",font=("times new roman", 16), background="#d9d9d9")
Number.grid(row=0 , column=2,padx=30, pady = 2)
Number_entry= Entry(frame, font=("times new roman", 16))
Number_entry.grid(row=0 , column=3,padx=8)
Bill_num= Label(frame,text="Bill_num",font=("times new roman", 16), background="#d9d9d9")
Bill_num.grid(row=0 , column=4,padx=30, pady = 2)
Bill_num_entry= Entry(frame, font=("times new roman", 16))
Bill_num_entry.grid(row=0 , column=5,padx=8)
submit = Button(frame, text="Submit", font=("times new roman", 16),width=8, command=submitnum)
submit.grid(row=0 , column=6,padx=40, pady = 8)

products_frame = Frame(windows)
products_frame.pack(fill=X)

Horror= LabelFrame(products_frame, text="Horror", font=("times new roman", 18, 'bold'), background="#d9d9d9")
Horror.grid(row=0 , column=0, padx = 10)

Killer_house = Label(Horror, text="Killer_house", font=("times new roman", 16), background="#d9d9d9")
Killer_house.grid(row=0 , column=0, padx=10, pady = 9)
Killer_house_entry= Entry(Horror, font=("times new roman", 16),width=8, bd=4)
Killer_house_entry.grid(row=0 , column=1, padx=20, pady = 9)
Killer_house_entry.insert(0,0)
Feast = Label(Horror, text="Feast", font=("times new roman", 16), background="#d9d9d9")
Feast.grid(row=1 , column=0, padx=10, pady = 9, sticky='w')
Feast_entry= Entry(Horror, font=("times new roman", 16),width=8, bd=4)
Feast_entry.grid(row=1 , column=1, padx=10, pady = 9)
Feast_entry.insert(0,0)
Bog_wife = Label(Horror, text="Bog_wife", font=("times new roman", 16), background="#d9d9d9")
Bog_wife.grid(row=2 , column=0, padx=10, pady = 9, sticky='w')
Bog_wife_entry= Entry(Horror, font=("times new roman", 16),width=8, bd=4)
Bog_wife_entry.grid(row=2 , column=1, padx=10, pady = 9)
Bog_wife_entry.insert(0,0)

Comedy= LabelFrame(products_frame, text="Comedy", font=("times new roman", 18, 'bold'), background="#d9d9d9")
Comedy.grid(row=0 , column=1, padx = 10)

Tina_fey = Label(Comedy, text="Tina_fey", font=("times new roman", 16), background="#d9d9d9")
Tina_fey.grid(row=0 , column=0, padx=10, pady = 9)
Tina_fey_entry= Entry(Comedy, font=("times new roman", 16),width=8, bd=4)
Tina_fey_entry.grid(row=0 , column=1, padx=10, pady = 9)
Tina_fey_entry.insert(0,0)
Omens = Label(Comedy, text="Omens", font=("times new roman", 16), background="#d9d9d9")
Omens.grid(row=1 , column=0, padx=10, pady = 9, sticky='w')
Omens_entry= Entry(Comedy, font=("times new roman", 16),width=8, bd=4)
Omens_entry.grid(row=1 , column=1, padx=10, pady = 9)
Omens_entry.insert(0,0)
Guncle = Label(Comedy, text="Guncle", font=("times new roman", 16), background="#d9d9d9")
Guncle.grid(row=2 , column=0, padx=10, pady = 9, sticky='w')
Guncle_entry= Entry(Comedy, font=("times new roman", 16),width=8, bd=4)
Guncle_entry.grid(row=2 , column=1, padx=10, pady = 9)
Guncle_entry.insert(0,0)

Fiction= LabelFrame(products_frame, text="Fiction", font=("times new roman", 18, 'bold'), background="#d9d9d9")
Fiction.grid(row=0 , column=2, padx = 10)

Davince_code= Label(Fiction, text="Davince_code", font=("times new roman", 16), background="#d9d9d9")
Davince_code.grid(row=0 , column=0, padx=10, pady = 9)
Davince_code_entry= Entry(Fiction, font=("times new roman", 16),width=8, bd=4)
Davince_code_entry.grid(row=0 , column=1, padx=10, pady = 9)
Davince_code_entry.insert(0,0)
Powerless = Label(Fiction, text="Powerless", font=("times new roman", 16), background="#d9d9d9")
Powerless.grid(row=1 , column=0, padx=10, pady = 9, sticky='w')
Powerless_entry= Entry(Fiction, font=("times new roman", 16),width=8, bd=4)
Powerless_entry.grid(row=1 , column=1, padx=10, pady = 9)
Powerless_entry.insert(0,0)
Dan_brown = Label(Fiction, text="Dan_brown", font=("times new roman", 16), background="#d9d9d9")
Dan_brown.grid(row=2 , column=0,padx=10, pady = 9, sticky='w')
Dan_brown_entry= Entry(Fiction, font=("times new roman", 16),width=8, bd=4)
Dan_brown_entry.grid(row=2 , column=1, padx=10, pady = 9)
Dan_brown_entry.insert(0,0)


bill_frame = Frame(products_frame, bd=8, relief = GROOVE)
bill_frame.grid(row=0, column =3)

bill = Label(bill_frame, text='Bill', font=("times new roman", 16))
bill.pack(fill=X)
scrollbar= Scrollbar(bill_frame,orient= VERTICAL)
scrollbar.pack(side= RIGHT, fill= Y)
text = Text(bill_frame, height = 20, width=54, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)


Bill_menu= LabelFrame(windows, text="Bill Menu", font=("times new roman", 18, 'bold'), background="#d9d9d9")
Bill_menu.pack( fill=X, pady=10)

Horrorp = Label(Bill_menu, text="Horror Price", font=("times new roman", 16), background="#d9d9d9")
Horrorp.grid(row=0 , column=0, padx=30, pady = 10)
Horrorp_entry= Entry(Bill_menu, font=("times new roman", 16))
Horrorp_entry.grid(row=0 , column=1, padx=8, pady = 10)
Comedyp = Label(Bill_menu, text="Comedy Price", font=("times new roman", 16), background="#d9d9d9")
Comedyp.grid(row=1 , column=0, padx=30, pady = 10)
Comedyp_entry= Entry(Bill_menu, font=("times new roman", 16))
Comedyp_entry.grid(row=1, column=1, padx=8, pady = 10)
Fictionp = Label(Bill_menu, text="Fiction Price", font=("times new roman", 16), background="#d9d9d9")
Fictionp.grid(row=2 , column=0, padx=30, pady = 10)
Fictionp_entry= Entry(Bill_menu, font=("times new roman", 16))
Fictionp_entry.grid(row=2 , column=1, padx=8, pady = 10)

framein = Frame(Bill_menu, height=10)
framein.grid(row=1, column=2, padx=60)
Total = Button(framein, text="Total", font=("times new roman", 16), width=8, command=total)
Total.grid(row=0 , column=0,padx=20, pady = 8)
Bill = Button(framein, text="Bill", font=("times new roman", 16), width=8, command= billing)
Bill.grid(row=0 , column=1,padx=20, pady = 8)
Print = Button(framein, text="Print", font=("times new roman", 16), width=8)
Print.grid(row=0, column=2,padx=20, pady = 8)
Email = Button(framein, text="Email", font=("times new roman", 16), width=8)
Email.grid(row=0 , column=3,padx=20, pady = 8)
Clear = Button(framein, text="Clear", font=("times new roman", 16), width=8)
Clear.grid(row=0 , column=4,padx=20, pady = 8)

windows.mainloop()
