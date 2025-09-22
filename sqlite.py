import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record,create table
cursor=connection.cursor()

#create table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

#insert some more records
cursor.cursor.execute('''INSERT INTO STUDENT VALUES ('John','Data Science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Alice','AI','B',85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Michael','Machine Learning','A',92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sophia','Cyber Security','C',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('David','Deep Learning','B',88)''')

# Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENTS''')
for row in data:
    print(row)

# commit the changes in database
connection.commit()
connection.close()

