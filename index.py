from Tkinter import *
import sqlite3
from tkMessageBox import *
#import splash

con = sqlite3.Connection('phonebook-db')
cur = con.cursor()

root=Tk()
root.wm_title('PhoneBook')
root.geometry('330x550')
Image = PhotoImage(file='p1.gif')
Label(root,text='             ').grid(row=1,column=0)
Label(root,text='PhoneBook GUI',font='Arial 20').grid(row=1,column=1)
#Label(root,text='             ').grid(row=2,column=1)


Label(root,image=Image).grid(row=3,column=1)
Label(root,text='             ').grid(row=4,column=1)
Label(root,text='First Name').grid(row=5,column=0)
fname=Entry(root).grid(row=5,column=1)
Label(root,text='Middle Name').grid(row=6,column=0)
mname=Entry(root).grid(row=6,column=1)
Label(root,text='Last Name').grid(row=7,column=0)
lname=Entry(root).grid(row=7,column=1)
Label(root,text='Company Name').grid(row=8,column=0)
comp_name = Entry(root).grid(row=8,column=1)
Label(root,text='Address').grid(row=9,column=0)
address = Entry(root).grid(row=9,column=1)
Label(root,text='City').grid(row=10,column=0)
city = Entry(root).grid(row=10,column=1)
Label(root,text='Pincode').grid(row=11,column=0)
pincode = Entry(root).grid(row=11,column=1)
Label(root,text='Select Phone Type',bg='plum1').grid(row=12,column=0)
phone_type=IntVar()
Radiobutton(root,text='Office',value=1,variable=phone_type,activebackground='seagreen1').grid(row=12,column=1)
Radiobutton(root,text='Home',value=2,variable=phone_type,activebackground='seagreen1').grid(row=13,column=1)
Radiobutton(root,text='Mobile',value=3,variable=phone_type,activebackground='seagreen1').grid(row=14,column=1)
Label(root,text='Phone Number').grid(row=15,column=0)
phone_number=Entry(root).grid(row=15,column=1)

email_type=IntVar()
Label(root,text='Email Type',bg='plum1').grid(row=16,column=0)
Radiobutton(root,text='Personal',value=1,variable=email_type,activebackground='seagreen1').grid(row=16,column=1)
Radiobutton(root,text='Office',value=2,variable=email_type,activebackground='seagreen1').grid(row=17,column=1)

Label(root,text='Email').grid(row=18,column=0)
email=Entry(root).grid(row=18,column=1)

#SQLITE3 implementation

root.mainloop()
