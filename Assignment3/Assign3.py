# Ananya Vittal
# 2270341

# pip install Faker
# pip install mysql-connector
import sys
import csv
from faker import Faker
import datetime
import random
from random import randint

# Database details
import mysql.connector

db = mysql.connector.connect(
    host="34.83.8.98",
    user="root",
    passwd="Hk1ru0HoKkjjzKzv",
    database="Assign3"
)


def dataGenerator(filename, records):
    headers = ["StudentName", "BirthDate", "Email", "Phone",
               "City", "State", "ZipCode", "Country", "ClassName",
               "ProfessorName", "DepartmentName"]
    classList = ["PSY", "BIO", "CPSC", "ECON", "MUS"]
    deptList = ["Crean", "Schmid", "Fowler", "Argyros", "CoPA"]
    generateData(filename, records, headers, classList, deptList)


def generateData(filename, records, headers, classList, deptList):
    fake = Faker("en_US")
    with open(filename + ".csv", "wt") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(int(records)):
            writer.writerow({
                "StudentName": fake.name(),
                "BirthDate": fake.date(pattern="%Y-%m-%d", end_datetime=datetime.date(2001, 1, 1)),
                "Email": fake.email(),
                "Phone": fake.phone_number(),
                "City": fake.city(),
                "State": fake.state(),
                "ZipCode": fake.zipcode(),
                "Country": fake.country(),
                "ClassName": random.choice(classList)+str(randint(100,500)),
                "ProfessorName": fake.name(),
                "DepartmentName": random.choice(deptList)
            })
    print("\nGenerated CSV!")


def dataImporter(filename):
    with open(filename + ".csv", "r") as csv_data:
        reader = csv.reader(csv_data)
        next(reader)
        for row in reader:
            mycursor = db.cursor()
            mycursor.execute("INSERT INTO Students(StudentName,BirthDate,Email,Phone,City,State,ZipCode,Country)"
                             "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],))
            mycursor.execute('SELECT * FROM Students;')
            all_rows = mycursor.fetchall()
            studentId = mycursor.lastrowid

            mycursor.execute("INSERT INTO Classes(ClassName)"    
                             "VALUES(%s)", (row[8],))
            mycursor.execute('SELECT * FROM Classes;')
            all_rows = mycursor.fetchall()
            classId = mycursor.lastrowid

            mycursor.execute("INSERT INTO ClassRegistration(StudentId, ClassId)"
                             "VALUES(%s,%s);", (studentId, classId))

            mycursor.execute("INSERT INTO Professors(ProfessorName)"
                             "VALUES(%s);", (row[9],))
            mycursor.execute('SELECT * FROM Classes;')
            all_rows = mycursor.fetchall()
            professorId = mycursor.lastrowid

            mycursor.execute("INSERT INTO Departments(ProfessorId, DepartmentName)"
                             "VALUES(%s,%s);", (professorId,row[10],))

    db.commit()
    db.close()
    print("\nData imported to database!\n")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        records = sys.argv[2]
        dataGenerator(filename, records)
        dataImporter(filename)
    else:
        print('Did not enter file name and number of tuples as command line parameters. Try again.')
