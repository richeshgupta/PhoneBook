#SQLITE3 implementation

############ table creation ################
cur.execute('PRAGMA foreign_keys = ON') #foreign key constraint on because of sqlite3 not default supporting it

a='create table if not exists person(id integer primary key AUTOINCREMENT,fname varchar(25),mname varchar(25),lname varchar(25),company varchar(30),website varchar(100) check(website like "%.%" ),b_date date check(b_date < DATE("now")),pin numeric,city varchar(25),street varchar(15)'
cur.execute(a) # Person Table

b ='create table if not exists phone_no(id integer primary key ,contact_type integer ,phone_number integer check(length(phone_number =10)),CONSTRAINT fk_pno foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(b) #phone_no table

r = 'create table if not exists email(id integer primary key ,email_type integer ,email_address varchar(50) check(email_address like "%_@_%._%"),CONSTRAINT fk_email foreign key(id) references person(id) ON DELETE CASCADE)'
cur.execute(r) #table email

#######################



# Saving data to Db
# a = [(fname.get(),mname.get(),lname.get(),comp_name.get(),website.get(),address.get(),city.get(),pincode.get(),phone_type,phone_number.get(),email_type.get(),email.get())]
#cur.execute('insert into person(')
# cur.execute('insert into person(fname,mname,lname,company,website,b_date,pin,hno,city,street,state,country) values("richesh","gupta","rg technos","richesh.com","2000-04-13","2080001","59/56","kanpur","birhana road","uttar pradesh","india")')


# #### Data from front end
firstn =fname.get()
middlen = mname.get()
lastn = lname.get()
comp_name = comp_name.get()
website_ = website.get()
address_var = address.get()
city_var = city.get()
pincode_var = pincode.get()
phone_type_var = phone_type.get()
phone_nummber_var = phone_number.get()
email_type_var = email_type.get()
email_var = email.get()
# print(firstn)

###############################################################
a=[(firstn,middlen,lastn,comp_name,address_var,city_var,pincode_var,website_)]
b=[(phone_type_var,phone_nummber_var,email_type_var,email_var)]
# query = 'insert into person'