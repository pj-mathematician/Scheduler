import localsql
from Logic import return_sched

cur = localsql.mycon.cursor()

def check_db():
    """
    Function that will check wheather the required tables exist in the database or not.
    Done so that user doesn't have to do more than just make the database and adjust localsql

    EDIT : We switched to an online MySQL server, so this is redundant at this point, but it will stay here anyway
    EDIT #2 : Due to some complications, we have switched back to the offline database(OOF)
    """
    cur.excecute("SHOW TABLES")
    table_list = cur.fetchall()

    if ("usepass",) not in table_list:
        query = "CREATE TABLE usepass(EMAIL VARCHAR(254) NOT NULL PRIMARY KEY, PASS VARCHAR(40) NOT NULL)"
        cur.execute(query)
        localsql.mycon.commit()

    if ("things_td",) not in table_list:
        query = "CREATE TABLE user_data(EMAIL VARCHAR(254) NOT NULL , SUBJECT VARCHAR(40) NOT NULL, TIME INT NOT NULL)"
        cur.execute(query)
        localsql.mycon.commit()

    if ("routine",) not in table_list:
        query = "CREATE TABLE routine(EMAIL VARCHAR(254) NOT NULL , TASK VARCHAR(40) NOT NULL, START_TIME INT NOT NULL, END_TIME INT NOT NULL)"
        cur.execute(query)
        localsql.mycon.commit()


def check(email,pwd):
    """Returns 0 if incorrect username :-
    0 if username incorrect :-O
    1 if everything is correct :-D
    2 if password is incorrect :-O """
    
    cur.execute('select exists(select * from usepass where email="%s")'%email)    #check for existance of a username
    
    rese = cur.fetchone()    #tuple containing a boolean value.For example--(1,) 
    if rese[0]:    #if 1
        cur.execute('select pass from usepass where email="%s"'%email)    #get the corresponding true password
        resp = cur.fetchone()    #tuple containing password.For example--('pass123',)

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

    query = "INSERT INTO usepass VALUES('{}', '{}')".format(items[0], items[1])

    cur.execute(query)
    localsql.mycon.commit()


def add_user_data(email, items):
    """
    Function to add the subjects and the time assigned to such tasks
    NOTE : items is a list of tuples containing records in the format => (<subject>, <time>)
           Time should be in the standard HH:MM:SS format
    """
    query = "INSERT INTO user_data VALUES('{}', %s, %s)".format(email)
    cur.executemany(query, items)
    localsql.mycon.commit()


def add_routine(email, tasks):
    """
    Function to add the daily routine into table "routine"
    NOTE : tasks is a list of tuples containing records in the format => (<event>, <time>)
           Time should be in the standard HH:MM:SS format
    """
    query = "INSERT INTO routine VALUES('{}', %s, %s)".format(email)
    cur.executemany(query, items)
    localsql.mycon.commit()


def return_schedule(email):
    """
    Function to retrieve the user data after succesful login, and give the corresponding schedule back to the user
    Based on the assumption that the email exists in the database
    """

    query = f"SELECT SUBJECT, TIME FROM user_data WHERE EMAIL = {email}"
    cur.execute(query)
    val = cur.fetchall()

    things_td = {}
    for i in val:
        temp = int(i[1])
        time = 60 * int(temp[:2:]) + int(temp[3:5:]) # Converting time to minutes
        things_td[i[0]] = time

    query = f"SELECT TASK, TIME FROM routine WHERE EMAIL = {email}"
    cur.execute(query)
    val = cur.fetchall()

    info = {}
    for i in val:
        temp = int(i[1])
        time = 60 * int(temp[:2:]) + int(temp[3:5:]) # Converting time to minutes
        info[i[0]] = time

    return return_sched(things_td, info)
