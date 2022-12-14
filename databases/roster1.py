import json
import sqlite3

con=sqlite3.connect('rosterdb1.sqlite')
cur=con.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User ;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Role;


CREATE TABLE User(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);
CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY(user_id,course_id)
);
''')

fname=input('enter the file name:')
fhand=open(fname).read()
json_data=json.loads(fhand)

for arr in json_data:
    name=arr[0]
    title=arr[1]
    role=arr[2]
    print((name,title))

    cur.execute('''
    INSERT OR IGNORE INTO User(name) VALUES (?)
    ''',(name,))
    cur.execute('SELECT id FROM User WHERE name=? ',(name,))
    user_id=cur.fetchone()[0]
    cur.execute('''
    INSERT OR IGNORE INTO Course(title) VALUES (?)
    ''',(title,))
    cur.execute('SELECT id FROM Course WHERE title=? ',(title,))
    course_id=cur.fetchone()[0]
    cur.execute('''
    INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES (?,?,?)
    ''',(user_id,course_id,role))

    con.commit()
