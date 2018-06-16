import sqlite3
import os

if os.path.exists('manager.db'):
	print('database file is already exist')
	exit(0)

conn = sqlite3.connect('manager.db')
print ("Opened database successfully")
c = conn.cursor()
c.execute('''create table POWER
       (user varchar(10) primary key,
       passwd text,
       authority int);''')
print ("Table created successfully")

c.execute('''insert into POWER (user, passwd, authority)
	values('admin','123', 0)''')
c.execute('''insert into POWER (user, passwd, authority)
	values('wuziqiang','123', 1)''')
print ("database init successfully");

conn.commit()
conn.close()