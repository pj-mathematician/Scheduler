import localsql

cur = localsql.mycon.cursor()


def check_db():
    """
    Function that will check wheather the required tables exist in the database or not.
    Done so that user doesn't have to do more than just make the database and adjust localsql

    EDIT : We switched to an online MySQL server, so this is redundant at this point, but it will stay here anyway
    """
    cur.excecute("SHOW TABLES")
    table_list = cur.fetchall()

    if ("usepass",) not in table_list:
        query = "CREATE TABLE usepass(EMAIL VARCHAR(254) NOT NULL PRIMARY KEY, PASS VARCHAR(40) NOT NULL)"
        cur.execute(query)


    if ("things_td",) not in table_list:
        query = "CREATE TABLE user_data(EMAIL VARCHAR(254) NOT NULL , SUBJECT VARCHAR(40) NOT NULL, TIME INT NOT NULL)"
        cur.execute(query)


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


def add_new_user(items):
    """
    Currently adding the name, email and passwd without verifying if they match with the 
    confirmed email id and passwd or not. It will be implemented only after the creation
    of the respective dialog boxes for such kind of mistakes.

    NOTE => 1) The order of the values may be different on your table. In that case create 
    an alternate line to execute the same code on your machine and comment it out. The 
    person using at the time has the responsibility of changing it according to their machine
    """

    email = items[0]
    query = "INSERT INTO usepass VALUES('{}', '{}')".format(items[0], items[1])

    cur.execute(query)
    localsql.mycon.commit()


def add_user_data(email, items):
    """
    Function to add the subjects and the time assigned to such tasks
    NOTE : items is a list of tuples containing records in the format => (<subject>, <time>)
    """
    query = "INSERT INTO user_data VALUES('{}', %s, %s)".format(email)
    cur.executemany(query, items)
    mycon.commit()