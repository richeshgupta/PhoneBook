from Tkinter import *
import sqlite3
from tkMessageBox import *
#import splash


con = sqlite3.Connection('pb-db')
cur = con.cursor()
cur.execute('PRAGMA foreign_keys = ON')
a='create table if not exists person(id integer primary key AUTOINCREMENT,fname varchar(25),mname varchar(25),lname varchar(25),company varchar(30),address text,city varchar(30),pin integer,website varchar(100))'
cur.execute(a)

b ='create table if not exists phone_no(id integer primary key ,contact_type integer ,phone_number integer check(length(phone_number =10)),CONSTRAINT fk_pno foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(b)

r = 'create table if not exists email(id integer primary key ,email_type integer ,email_address varchar(50) ,CONSTRAINT fk_email foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(r)


root=Tk()
root.wm_title('PhoneBook')
root.geometry('330x550')
Image = PhotoImage(file='p1.gif')
Label(root,text='             ').grid(row=1,column=0)
Label(root,text='PhoneBook GUI',font='Arial 20').grid(row=1,column=1)
#Label(root,text='             ').grid(row=2,column=1)


p1 = Label(root,image=Image)
p1.grid(row=3,column=1)
p2 = Label(root,text='             ')
p2.grid(row=4,column=1)
p3=Label(root,text='First Name')
p3.grid(row=5,column=0)
fname=Entry(root)
fname.grid(row=5,column=1)
p4=Label(root,text='Middle Name')
p4.grid(row=6,column=0)
mname=Entry(root)
mname.grid(row=6,column=1)
p5=Label(root,text='Last Name')
p5.grid(row=7,column=0)
lname=Entry(root)
lname.grid(row=7,column=1)
p6=Label(root,text='Company Name')
p6.grid(row=8,column=0)

comp_name = Entry(root)
comp_name.grid(row=8,column=1)

p7 = Label(root,text='Address')
p7.grid(row=9,column=0)

address = Entry(root)
address.grid(row=9,column=1)
p8=Label(root,text='City')
p8.grid(row=10,column=0)

city = Entry(root)
city.grid(row=10,column=1)

p9=Label(root,text='Pincode')
p9.grid(row=11,column=0)

pincode = Entry(root)
pincode.grid(row=11,column=1)

p10=Label(root,text='Select Phone Type',bg='plum1')
p10.grid(row=12,column=0)
phone_type=IntVar()
Radiobutton(root,text='Office',value=1,variable=phone_type,activebackground='seagreen1').grid(row=12,column=1)
Radiobutton(root,text='Home',value=2,variable=phone_type,activebackground='seagreen1').grid(row=13,column=1)
Radiobutton(root,text='Mobile',value=3,variable=phone_type,activebackground='seagreen1').grid(row=14,column=1)
Label(root,text='Phone Number').grid(row=15,column=0)
phone_number=Entry(root)
phone_number.grid(row=15,column=1)

email_type=IntVar()
Label(root,text='Email Type',bg='plum1').grid(row=16,column=0)
Radiobutton(root,text='Personal',value=1,variable=email_type,activebackground='seagreen1').grid(row=16,column=1)
Radiobutton(root,text='Office',value=2,variable=email_type,activebackground='seagreen1').grid(row=17,column=1)


p100=Label(root,text='Email')
p100.grid(row=18,column=0)
email=Entry(root)
email.grid(row=18,column=1)

p101=Label(root,text='Website')
p101.grid(row=19,column=0)
website=Entry(root)
website.grid(row=19,column=1)

# # b_date = StringVar()
# p102=Label(root,text='Birthdate')
# p102.grid(row=20,column=0)
# b_date=Entry(root)
# b_date.grid(row=20,column=1)

def save():
	fn,mn,ln,cn,add,cit,pin,web=fname.get(),mname.get(),lname.get(),comp_name.get(),address.get(),city.get(),pincode.get(),website.get()
	query=[(fn,mn,ln,cn,add,cit,pin,web)]
	g ='insert into person(fname,mname,lname,company,address,city,pin,website) values(?,?,?,?,?,?,?,?)'

	print("query : ",query)
	cur.executemany(g,query)
	
Button(root,text='Insert',command=save).grid(row=22,column=1)
root.mainloop()