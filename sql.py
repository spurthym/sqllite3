import sqlite3

#define connection and cursor

connection=sqlite3.connect('courier.db ')
c=connection.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS delivery(name text,item text,phno int,salary int)')

def data_entry():
	c.execute("INSERT INTO delivery VALUES('raj','laptop',84735786 ,2000)" )
	c.execute("INSERT INTO delivery VALUES('leo','bicycle',94851234 ,1000)" )

	connection.commit()
	

def read_data():

	data=c.execute('SELECT * FROM delivery ')
	print("The available delivery boys records are :")
	for record in data:
		print(record)
	sal=c.execute('SELECT salary FROM delivery')
	sal_list=[int(a[0]) for a in sal]
	avg=sum(sal_list)/len(sal_list)

	print('the average salary of the current delivery boys is:{0}'.format(avg))


create_table()
data_entry()
read_data()
