import mysql.connector as connector

mycon = connector.connect(host='db4free.net', user='mdscheduler', passwd='password', database='mdscheduler',port='3306')
if mycon.is_connected():
	print('Connected')
