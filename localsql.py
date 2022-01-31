import mysql.connector as connector

#mycon = connector.connect(host='db4free.net', user='mdscheduler', passwd='password', database='mdscheduler',port='3306')
mycon = connector.connect(host='localhost', user='root', passwd='*****', database='scheduler',port='3306')

if mycon.is_connected():
	print('Connected')
