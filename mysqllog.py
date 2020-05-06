import localsql
cur=localsql.mycon.cursor()

def check(email,pwd):
    ##Returns 0 if incorrect username, 1 if everything is correct :-D, 2 if password is incorrect :-O##
    
    cur.execute('select exists(select * from usepass where email="%s")'%email)    #check for existance of a username
    
    rese=cur.fetchone()    #tuple containing a boolean value.For example--(1,) 
    if rese[0]:    #if 1
        cur.execute('select pass from usepass where email="%s"'%email)    #get the corresponding true password
        resp=cur.fetchone()    #tuple containing password.For example--('pass123',)
        if pwd==resp[0]:    # if input password == true password
            return 1    # PASSWORD CORRECT
        else:
            return 2    # PASSWORD INCORRECT
           
    else:    
        return 0       # USERNAME INCORRECT
