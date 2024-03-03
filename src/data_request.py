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
#print(raw_student_population)