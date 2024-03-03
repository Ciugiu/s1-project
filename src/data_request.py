import mysql.connector
from src.data_request_ids import host, user, password, database

def connect():
    return mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )

def retrieve(query: str, params):
    mysql = connect()
    cursor = mysql.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    mysql.close()
    return result
