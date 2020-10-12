import mysql.connector as connector

mycon = connector.connect(host='sql12.freesqldatabase.com', user='sql12370259', passwd='ZrNzpx8BZq', database='sql12370259',port='3306')
if mycon.is_connected():
	print('Connected')
