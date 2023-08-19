

import sqlite3 


conn = sqlite3.connect("datasecret.db")

cursor= conn.cursor()

def createTable():
    cursor.execute("DROP TABLE IF EXISTS SECRET")
    # create query

    query = """CREATE TABLE SECRET(
        ID INT PRIMARY KEY NOT NULL,
        NAME CHAR(20) NOT NULL, 
        ROLL CHAR(20), 
        ADDRESS CHAR(50), 
        CLASS CHAR(20) )"""
    cursor.execute(query)
# commit and close
    conn.commit()
    conn.close()

def selectesecret():
    cursor.execute("select * from SECRET")
    print(cursor.fetchall())
    conn.close()

def deletesecret():
    conn.execute("DELETE from STUDENT where ID = 2;")
    conn.commit()

def updatesecret(id):
    conn.execute(f"UPDATE STUDENT set ROLL = 005 where ID = {id} ")
    conn.commit()



def insertSecret(id,name,roll,address,clas):
    query = ('INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) '
         'VALUES (:ID, :NAME, :ROLL, :ADDRESS, :CLASS);')
    params = {
        'ID': id,
        'NAME': name,
        'ROLL': roll,
        'ADDRESS': address,
        'CLASS': clas
    }
    conn.execute(query, params)
    conn.close()
