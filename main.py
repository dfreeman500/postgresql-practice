#https://www.postgresqltutorial.com/postgresql-python/connect/
#https://www.youtube.com/watch?v=OOSl2jeAA5U
#https://www.youtube.com/watch?v=OOSl2jeAA5U

import psycopg2
import psycopg2.extras


conn = psycopg2.connect("dbname=suppliers user=postgres password=password") # sets updb, user/pass
cur = conn.cursor() # lets execute statements create/insert

# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")  #runs once
# cur.execute("INSERT INTO student (name) VALUES(%s)",("Anthony",)) #pass in a tuple
# cur.execute("INSERT INTO student (name) VALUES(%s)",("Bob",)) #pass in a tuple
# cur.execute("INSERT INTO student (name) VALUES(%s)",("Christina",)) #pass in a tuple

cur.execute("SELECT * from student;") #fetches all items 
print(cur.fetchall())

cur.execute("SELECT * from student WHERE id = %s;",(1,)) #fetches one item where id = 1
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()