# importing module
import sqlite3
from sqlite3 import Error

import os

# Creating a function


def takeinput():
    while True:
        query = input("\nEnter Q to Quit\nEnter A to Add student\nEnter V to view students\nEnter T for view total number of students\nEnter U for update\nEnter D for Delete student\n")

        if(query == "Q"):
            break
        elif (query == "A"):
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            name = input("Enter Students Name\n")
            age = input("Enter students Age\n")
            height = input("Enter students Height\n")
            cursor.execute(
                """INSERT INTO students(student_name,student_height,student_age )VALUES(?,?,?) """, (name, age, height))

            conn.commit()
            print('Data entered Successfully')

        elif(query == 'V'):
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            print("Students Details:")
            print("ID----NAME----AGE------HEIGHT")
            for row in rows:
                print(row)

        elif(query == "T"):
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            cursor = cursor.execute("SELECT * FROM students")
            print(f"Total Number of Students is {len(cursor.fetchall())}")

        elif(query == "U"):
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            print("Students Details:")
            print("ID----NAME----AGE------HEIGHT")
            for row in rows:
                print(row)

            # Update
            print()
            Id = input("Enter student id\n")
            height = input("Enter student Height\n")
            age = input("Enter student Age\n")

            cursor.execute(
                '''UPDATE students SET student_age = ? ,student_height = ? WHERE student_id = ? ''', (height, age, Id))
            conn.commit()
            print("Record Update Successfully")

        elif(query == "D"):
            conn = sqlite3.connect('mydatabase.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            print("Students Details:")
            print("ID----NAME----AGE------HEIGHT")
            for row in rows:
                print(row)

            # Delete
            print()
            id = input("Enter Student ID\n")

            cursor.execute(
                '''DELETE FROM students WHERE student_id = ?''', (id))
            conn.commit()
            print("Record Delete Successfully")


if not os.path.isfile('mydatabase.db'):

    # creating new database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    # creating table
    cursor.execute(
        """CREATE TABLE students(student_id INTEGER PRIMARY KEY AUTOINCREMENT,student_name char(40),student_height char(35),student_age char(35)); """
    )

    takeinput()

else:
    takeinput()
