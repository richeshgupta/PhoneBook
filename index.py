
from Tkinter import *
import sqlite3
from tkMessageBox import *
import splash

tab1=[]
tab2=[]
tab3=[]

ikd = 0
con = sqlite3.Connection('pb-db')
cur = con.cursor()

cur.execute('PRAGMA foreign_keys = ON')
a='create table if not exists person(id integer primary key AUTOINCREMENT,fname varchar(25),mname varchar(25),lname varchar(25),company varchar(30),address text,city varchar(30),pin integer,website varchar(100))'
cur.execute(a)

b ='create table if not exists phone_no(id integer primary key ,contact_type varchar(30) ,phone_number integer,CONSTRAINT fk_pno foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(b)

r = 'create table if not exists email(id integer primary key ,email_type varchar(30) ,email_address varchar(50) ,CONSTRAINT fk_email foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(r)



root=Tk()
root.wm_title('PhoneBook')
root.geometry('380x650')
Image = PhotoImage(file='p1.gif')
Label(root,text='             ').grid(row=1,column=0)
Label(root,text='PhoneBook GUI',font="Arial 20").grid(row=1,column=1)



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

k=[]
def save():
	fn,mn,ln,cn,add,cit,pin,web=fname.get(),mname.get(),lname.get(),comp_name.get(),address.get(),city.get(),pincode.get(),website.get()
	query=[(fn,mn,ln,cn,add,cit,pin,web)]
	global ikd
	check = 'select * from person where id = {}'.format(ikd)
	cur.execute(check)
	check = cur.fetchall()
	if len(check)>0:
		qq = 'delete from person where id = {}'.format(ikd)
		ikd = -1
		cur.execute(qq)
		showinfo('Updated Successfully!','Updated Successfully!')

	g ='insert into person(fname,mname,lname,company,address,city,pin,website) values(?,?,?,?,?,?,?,?)'
	# print("query : ",query)
	cur.executemany(g,query)
	q2 = 'select max(id) from person'
	cur.execute(q2)
	f_id = cur.fetchall()
	f_id = f_id[0][0]

	phone_type_a = phone_type.get()
	phone_no_a = phone_number.get()
	
	
	
	if phone_no_a is not '':
		if phone_type_a !=0:
			if phone_type_a ==1:
				query2 = 'insert into phone_no values(?,"Office",?)'
			elif phone_type_a ==2:
				query2='insert into phone_no values(?,"Home",?)'
			elif phone_type_a ==3:
				query2='insert into phone_no values(?,"Mobile",?)'
		else:
			query2='insert into phone_no values(?,"Mobile",?)'
		var2 = [(f_id),(phone_no_a)]
		cur.execute(query2,var2)
		cur.execute('select * from phone_no')
		# print(cur.fetchall())
		
	## email table
	email_type_a  = email_type.get()
	email_a = email.get()
	if email_a is not '':
		if email_type_a is not 0:
			if email_type_a ==1:
				query3 = 'insert into email values(?,"Personal",?)'
			elif email_type_a ==2:
				query3 = 'insert into email values(?,"Office",?)'
		else:
			query3 = 'insert into email values(?,"Personal",?)'
		var3 = [(f_id),(email_a)]
		cur.execute(query3,var3)
		# print(var3)
		if len(check)==0:
			showinfo('Saved Successfully!','Saved Successfully!')
	con.commit()

	##deleting ALL the entries
	fname.delete(0,END)
	mname.delete(0,END)
	lname.delete(0,END)
	comp_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	pincode.delete(0,END)
	website.delete(0,END)
	email.delete(0,END)
	phone_number.delete(0,END)
	email_type.set(None)
	phone_type.set(None)
	##########################


def close():
	root.destroy()

def search():
	top = Toplevel()
	top.wm_title('Search contacts')
	top.geometry('460x850')
	Label(top,text='Search Contacts',font="Arial 20").grid(row=1,column=2)
	Label(top,text='Enter name').grid(row=2,column=1)
	search=Entry(top)
	search.grid(row=2,column=2)
	lb = Listbox(top,width=60,height=30)
	lb.grid(row=3,column=2)
	def fire(e=0):
		q = search.get()
		lb.delete(0,END)
		x = "select id,fname,mname,lname from person where fname like '%{}%' or mname like '%{}%' or lname like '%{}%'".format(q,q,q,phone_number.get())
		cur.execute(x)
		global k
		k = cur.fetchall()

		# print(k)
		i = 0

		while(i<len(k)):
			fn = k[i][1]+' '+k[i][2]+' '+k[i][3]
			lb.insert(0,fn)
			i+=1

	def showing(e=0):
		global tab1,tab2,tab3
		per = lb.curselection()
		ind = per[0]
		lb.delete(0,END)
		global k
		ind = len(k)-ind-1
		global ikd
		ikd = k[ind][0]
		top2 = Toplevel()
		top2.geometry('500x400')
		cur.execute('select * from person where id = ?',(ikd,))
		tab1  = cur.fetchall()
		print(tab1)
		Label(top2,text='                              ').grid(row=0,column=0)
		Label(top2,text='Search Result',font="Arial 25").grid(row=0,column=1)
		Label(top2,text="Name : {}".format((tab1[0][1]+" "+tab1[0][2]+" "+tab1[0][3])),font="Arial 16").grid(row=1,column=1)
		Label(top2,text="Company : {}".format(tab1[0][4]),font="Arial 16").grid(row=2,column=1)
		Label(top2,text="Address : {}".format(tab1[0][5]),font="Arial 16").grid(row=3,column=1)
		Label(top2,text="City : {}".format(tab1[0][6]),font="Arial 16").grid(row=4,column=1)
		Label(top2,text="Website : {}".format(tab1[0][8]),font="Arial 16").grid(row=5,column=1)
		cur.execute('select * from phone_no where id = ?',(ikd,))
		tab2  = cur.fetchall()
		print(tab2)

		if len(tab2)!=0:
			Label(top2,text="Phone Type : {}".format(tab2[0][1]),font="Arial 16").grid(row=6,column=1)
			Label(top2,text="Phone Number : {}".format(tab2[0][2]),font="Arial 16").grid(row=7,column=1)
		else:
			Label(top2,text="Phone Type : Not Entered Yet",font="Arial 16").grid(row=6,column=1)
			Label(top2,text="Phone Number : Not Entered Yet",font="Arial 16").grid(row=7,column=1)
		
		cur.execute('select * from email where id = ?',(ikd,))

		tab3 = cur.fetchall()

		if len(tab3)!=0:
			Label(top2,text="Email Type : {}".format(tab3[0][1]),font="Arial 16").grid(row=8,column=1)
			Label(top2,text="Email Id : {}".format(tab3[0][2]),font="Arial 16").grid(row=9,column=1)
		else :
			Label(top2,text="Email Type : Not Entered Yet",font="Arial 16").grid(row=8,column=1)
			Label(top2,text="Email Id : Not Entered Yet",font="Arial 16").grid(row=9,column=1)
		
		def edit():
			top2.destroy()
			top.destroy()
			fname.delete(0,END)
			fname.insert(0,(tab1[0][1]))
			mname.delete(0,END)
			mname.insert(0,(tab1[0][2]))
			lname.delete(0,END)
			lname.insert(0,(tab1[0][3]))
			comp_name.delete(0,END)
			comp_name.insert(0,(tab1[0][4]))
			address.delete(0,END)
			address.insert(0,(tab1[0][5]))
			city.delete(0,END)
			city.insert(0,(tab1[0][6]))
			pincode.delete(0,END)
			pincode.insert(0,(tab1[0][7]))
			website.delete(0,END)
			website.insert(0,(tab1[0][8]))
			email.delete(0,END)

			if len(tab3)!=0:
				email.insert(0,(tab3[0][2]))
				email_type_a = tab3[0][1]

				if email_type_a =='Personal':
					email_type.set(1)
				elif email_type_a == 'Office':
					email_type.set(2)
			if len(tab2)!=0:
				phone_number.delete(0,END)
				phone_number.insert(0,(tab2[0][2]))
				phone_type_a = tab2[0][1]
				
				if phone_type_a =='Office':
					phone_type.set(1)
				elif phone_type_a == 'Home':
					phone_type.set(2)
				elif phone_type_a == 'Mobile':
					phone_type.set(3)
			con.commit()
		def delete_tuple():
			to_delete = askquestion('Do you really want to delete it?','Do you really want to delete it?',icon='warning')
			if to_delete == 'yes':
				global ikd
				delete_query = 'delete from person where id = {}'.format(ikd)
				cur.execute(delete_query)
				ikd = -1
				con.commit()
				showinfo('Deleted Successfully!','Deleted Successfully!')
				top2.destroy()
		Button(top2,text="Edit",command=edit).grid(row=10,column=1)
		Button(top2,text="Delete",command=delete_tuple,fg="red").grid(row=11,column=1,pady=5)		
	search.bind('<Button-1>',fire)
	top.bind('<Key>',fire)
	lb.bind('<Double-Button-1>',showing)

def reset():
			fname.delete(0,END)
			mname.delete(0,END)
			lname.delete(0,END)
			comp_name.delete(0,END)
			address.delete(0,END)
			city.delete(0,END)
			pincode.delete(0,END)
			website.delete(0,END)
			email.delete(0,END)
			email_type.set(0)
			phone_type.set(0)

Button(root,text='Insert',command=save).grid(row=22,column=0,pady=5)
Button(root,text='Search',command=search).grid(row=22,column=1,pady=5)
Button(root,text="Edit",command=search).grid(row=22,column=2,pady=5)
Button(root,text="Reset",command=reset).grid(row=23,column=1,pady=5)
Button(root,text='Exit',command=close).grid(row=25,column=1,pady=5)
root.mainloop()
