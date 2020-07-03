# Scheduler
Scheduler made in kivy language using kivyMD library.

To run the program:-

1) Make a localsql.py file including the connection object as mycon. Make a database called "scheduler" and create a table in that table called usepass with the following columns:-

    a) Name - Email, Type - varchar(254), Key - Primary, Not Null
    
    b) Name - Password, Type - varchar(20), Not Null

Note:-

1) make a localsql.py file including the connection object as mycon

2) Made the signup page functional. you should have only two attributes in the usepass table i.e.email and pass 

3) Need to add option to make the table for the data of the user in the program itself, and also for making the usepass table(currently, the user has to manually create the table). Currently only storing the user's email and password. 

4) Shortcut present in main.py is only for the developers. It is NOT meant for the normal user. 
