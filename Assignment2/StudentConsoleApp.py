# https://stackoverflow.com/questions/60714669/using-the-sql-like-operator-with-tuple-insertion
# Ananya Vittal
# 2270341
import sqlite3
import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_columns', None)

# Connect to database
conn = sqlite3.connect('StudentDB.sqlite')
c = conn.cursor()  # allows python code to execute SQL statements


# a) Display all Students and their attributes
def one():
    c.execute('SELECT StudentId,FirstName,LastName,GPA,Major,FacultyAdvisor FROM Student WHERE isDeleted = 0')

    all_rows = c.fetchall()
    df = DataFrame(all_rows,
                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor'])
    print(df)


# b) Create Students - ############################### Fix constraints for Major and Faculty Advisor
def two():
    while True:
        fname = input('First Name: ')
        if len(fname.strip()) == 0 or len(fname.strip()) > 32 or not fname.isalpha():
            continue
        else:
            break
    while True:
        lname = input('Last Name: ')
        if len(lname.strip()) == 0 or len(lname.strip()) > 32 or not lname.isalpha():
            continue
        else:
            break
    while True:
        try:
            gpa = float(input('GPA: '))
        except ValueError:
            continue
        else:
            break
    while True:
        major = input('Major: ')
        if len(major.strip()) == 0 or len(major.strip()) > 16:
            continue
        else:
            break
    while True:
        advisor = input('Faculty Advisor: ')
        if len(advisor.strip()) == 0 or len(advisor.strip()) > 32:
            continue
        else:
            break
    isdeleted = False
    c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted')"
              "VALUES(?,?,?,?,?,?)", (fname, lname, gpa, major, advisor, isdeleted,))
    conn.commit()
    studentId = c.lastrowid
    print('\nRecord Created, ID:', studentId)


# c) Update Students
def three():
    display_choice = input('Would you like to update the Student\'s (1)Major or (2)Advisor?: ')
    if display_choice == '1':
        while True:
            student_param = input("Enter the StudentID of the record you would like to update: ")
            if len(student_param.strip()) == 0:
                continue
            else:
                c.execute("SELECT COUNT(StudentId) FROM Student WHERE isDeleted = 0 AND StudentId = ?",
                          (student_param,))
                exists = c.fetchall()
                if exists == [(0,)]:
                    print('Record does not exist in database. Try again')
                    continue
                else:
                    break
        while True:
            major_param = input("Enter the updated Major: ")
            if len(major_param.strip()) == 0:
                continue
            else:
                break
        c.execute("UPDATE Student SET Major = ? WHERE isDeleted = 0 AND StudentId = ?", (major_param, student_param,))
        conn.commit()
        print("\nRecord", student_param, "updated")
        options[1]()
    elif display_choice == '2':
        while True:
            student_param = input("Enter the StudentID of the record you would like to update: ")
            if len(student_param.strip()) == 0:
                continue
            else:
                c.execute("SELECT COUNT(StudentId) FROM Student WHERE isDeleted = 0 AND StudentId = ?",
                          (student_param,))
                exists = c.fetchall()
                if exists == [(0,)]:
                    print('Record does not exist in database. Try again')
                    continue
                else:
                    break
        while True:
            advisor_param = input("Enter the updated Advisor: ")
            if len(advisor_param.strip()) == 0:
                continue
            else:
                break
        c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE isDeleted = 0 AND StudentId = ?",
                  (advisor_param, student_param,))
        conn.commit()
        print("\nRecord", student_param, "updated")
        options[1]()
    else:
        print('Try again')
        options[3]()


# d) Delete Students by StudentId
def four():
    while True:
        student_param = input('Enter the StudentID of the record you would like to delete: ')
        if len(student_param.strip()) == 0:
            continue
        else:
            c.execute("SELECT COUNT(StudentId) FROM Student WHERE isDeleted = 0 AND StudentId = ?", (student_param,))
            exists = c.fetchall()
            if exists == [(0,)]:
                print('Record does not exist in database. Try again')
                continue
            else:
                break
    c.execute("UPDATE Student SET isDeleted = 1 WHERE StudentId = ?", (student_param,))
    conn.commit()
    print("\nRecord", student_param, "deleted")
    options[1]()


# e) Search/display Students by Major, GPA, or Advisor 
def five():
    display_choice = input('Would you like to display students by (1)Major, (2)GPA, or (3)Advisor?: ')
    if display_choice == '1':
        while True:
            major_param = input('Enter Major you would like to display: ')
            if len(major_param.strip()) == 0:
                continue
            else:
                c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM Student WHERE isDeleted = 0 AND Major LIKE ?',(f'%{major_param}%',))
                all_rows = c.fetchall()
                if all_rows == []:
                    print('Record does not exist in database. Try again')
                    continue
                else:
                    break
        df = DataFrame(all_rows, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor'])
        print(df)
    elif display_choice == '2':
        while True:
            gpa_param = input('Enter GPA you would like to display: ')
            if len(gpa_param.strip()) == 0:
                continue
            else:
                c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM Student WHERE isDeleted = 0 AND GPA LIKE ?',(f'%{gpa_param}%',))
                all_rows = c.fetchall()
                if all_rows == []:
                    print('Record does not exist in database. Try again')
                    continue
                else:
                    break
        df = DataFrame(all_rows, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor'])
        print(df)
    elif display_choice == '3':
        while True:
            advisor_param = input('Enter Faculty Advisor you would like to display: ')
            if len(advisor_param.strip()) == 0:
                continue
            else:
                c.execute(
                    'SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM Student WHERE isDeleted = 0 AND FacultyAdvisor LIKE ?',(f'%{advisor_param}%',))
                all_rows = c.fetchall()
                if all_rows == []:
                    print('Record does not exist in database. Try again')
                    continue
                else:
                    break
        df = DataFrame(all_rows, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor'])
        print(df)
    else:
        print('Try again')
        options[5]()


# Menu option numbers
options = {1: one,
           2: two,
           3: three,
           4: four,
           5: five
           }

# Menu that displays user options
menu = input('Welcome! Would you like to view the menu? (Y/N): ')
while menu != 'N' and menu != 'n':
    print('\nMenu: ')
    print('#1: Display all Students and their attributes')
    print('#2: Create Students')
    print('#3: Update Students by Major or Advisor')
    print('#4: Delete Students by StudentId')
    print('#5: Search/display Students by Major, GPA, or Advisor')
    print('#6: Exit Application')
    number = input('\nEnter the number of the option you want: ')
    if number == '1':
        options[1]()
    elif number == '2':
        options[2]()
    elif number == '3':
        options[3]()
    elif number == '4':
        options[4]()
    elif number == '5':
        options[5]()
    elif number == '6':
        print('Exiting...')
        exit()
