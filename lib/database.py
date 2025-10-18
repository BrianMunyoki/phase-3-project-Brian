import sqlite3 # built in library that lets python talk to SQLITE database
from pathlib import Path #helps us find the correct location of our database 

DB_PATH= Path(__file__). resolve().parents[1]/"db"/"database.db" #this finds our db/database file automatically  even if our procjcet run from a different location.

CONN=sqlite3.connect(DB_PATH) #Conn is the connection to the database
CURSOR=CONN.cursor() # cursor is the tool for sending sql commands. 
def create_tables(): # here we have created 3 tables nameley: students, coursers and enrollments. Note: enrollment connects students and courses :many to many 
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS students( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT UNIQUE,
        instructor TEXT
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS enrollments(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES student(id)
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
    """)
    CONN.commit()
    #the command IF NOT EXISTS prevents errors if you run this twice while onn.commit() permanetly saves the changes. 