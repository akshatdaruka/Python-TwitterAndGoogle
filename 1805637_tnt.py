#NAME: AKSHAT DARUKA
#ROLL: 1805637

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()

#Answer 1:

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    if x =='SCE-KIIT':
        print('Database SCE-KIIT Exists')
        break

#Answer 2:

mycursor.execute('DROP DATABASE IF EXISTS SCE-KIIT')

#Answer 3:

mycursor.execute('CREATE DATABASE SCE-KIIT')

#Answer 4:

mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="SCE-KIIT"
)


mycursor.execute("SHOW TABLES")
for x in mycursor:
    if x =='student':
        print('Table student Exists')
        break

#Answer 5:

mycursor.execute('DROP TABLE IF EXISTS student')
mydb1.commit()

#Answer 6:

sql1= "CREATE TABLE student(roll INT, name VARCHAR(50), branch VARCHAR(30), semester INT, CGPA FLOAT)"

mycursor.execute(sql1)
mydb1.commit()

#Answer 7:

sql2 ="INSERT INTO students VALUES(%s %s %s %s %s)"
val=[
(1,'Roger','CSE',4,9.8),
(2,'Rafa','ETC',5,9.2),
(3,'Andy','CSSE',6,9.1),
(4,'Stan','CSE',2,9.0),
(5,'Novak','CSSE',4,9.1),
(6,'Juan','ETC',3,9.2),
(7,'Dominic','CSE',5,9.4),
(8,'Alex','CSSE',4,9.1),
(9,'Stephanos','ETC',6,9.3),
(10,'Pete','CSSE',4,9.2),
]
mycursor.executemany(sql2,val)
mydb1.commit()

#Answer 8:

sql3 = "UPDATE students SET roll=11,name=Tim,branch=IT,semester=7,CGPA=9.1 WHERE roll=%s"
adr=("3",)
mycursor.execute(sql3,adr)
mydb1.commit()

#Answer 9:

sql4 = "DELETE FROM students WHERE roll = %s"
adr = ("5", )
mycursor.execute(sql, adr)
mydb1.commit()
sql5 = "DELETE FROM students WHERE branch = %s"
adr = ("CSSE", )
mycursor.execute(sql5, adr)
mydb1.commit()

#Answer 10:

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
