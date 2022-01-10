import sqlite3

conn = sqlite3.connect('login.db')
print ("Opened database successfully");

#conn.execute("INSERT INTO logintest(user_id,username,password) VALUES(1,'MINDA','123')") # INSERTING INTO SQLLITE3 TABLE
 
cursor = conn.execute("SELECT * FROM login")                                       #FETCHING RECORDS FROM DATABASE                                        
for row in cursor:                                    
	print(row[0],row[1],row[2])

#conn.execute("UPDATE logintest set username = 'manvinder' where user_id = 1")            #UPDATING RECORDS

#conn.execute("DELETE from logintest where user_id = 1")                                 #DELETING A RECORD FROM DATABASE

'''
cursor = conn.execute("SELECT * FROM logintest")                                      #CHECKING IF A TABLE IS EMPTY 
print(len(cursor.fetchall()))
'''



conn.commit()
conn.close()