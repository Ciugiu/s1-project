<<<<<<< HEAD
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="project"
    )

def retrieve(query: str):
    mysql = connect()
    cursor = mysql.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    mysql.close()
    return result

#with open('src/active_population', 'r') as file:
#    raw_student_population = retrieve(file.read())
#
=======
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="project"
    )

def retrieve(query: str):
    mysql = connect()
    cursor = mysql.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    mysql.close()
    return result

#with open('src/active_population', 'r') as file:
#    raw_student_population = retrieve(file.read())
#
>>>>>>> e8b59a0471c883f3840e95294ddf0e06a44744d4
#print(raw_student_population)