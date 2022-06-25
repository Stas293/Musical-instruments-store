import numpy as np
import mysql.connector
from program.Model import Status


# Admin
def insert_status(status, connection):
    try:
        cursor = connection.cursor()
        textSQL = "INSERT INTO status (code, name, closed) VALUES (%s, %s, %s) "
        cursor.execute(textSQL, (status.code, status.name, status.isClosed))
        connection.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def find_status_by_name(name, connection):
    try:
        cursor = connection.cursor()
        txtSQL = "SELECT * FROM status WHERE name = %s"
        cursor.execute(txtSQL, (name,))
        status = cursor.fetchone()
        cursor.close()
        status = Status(status[0], status[1], status[2], status[3])
        return status
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def find_status_by_id(id, connection):
    try:
        cursor = connection.cursor()
        textSQL = "SELECT * FROM status WHERE status_id = %s"
        cursor.execute(textSQL, (id,))
        status = cursor.fetchone()
        cursor.close()
        status = Status(status[0], status[1], status[2], status[3])
        return status
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def find_all_statuses(connection):
    try:
        cursor = connection.cursor()
        txtSQL = "SELECT * FROM status"
        cursor.execute(txtSQL)
        statuses = cursor.fetchall()
        cursor.close()
        status = []
        for s in statuses:
            st = Status(s[0], s[1], s[2], s[3])
            status.append(st)
        return status
    except mysql.connector.Error as e:
        print(e)
        return False


# Admin
def update_status(status, connection, name):
    try:
        cursor = connection.cursor()
        textSQL = "SELECT status_id FROM status WHERE name = %s"
        statusId = cursor.execute(textSQL, (name,))
        textSQL = "UPDATE status SET code = %s, name = %s, closed = %s WHERE status_id = %s"
        cursor.execute(textSQL, (status.code, status.name, status.isClosed, statusId))
        connection.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def possible_stat(status, connection):
    try:
        cursor = connection.cursor()
        textSQL = "SELECT status.* FROM next_status join `status` ON next_status.next_status_id = status.status_id where next_status.status_id = %s"
        cursor.execute(textSQL, (status.statusId,))
        status = cursor.fetchone()
        cursor.close()
        statuses = Status(status[0], status[1], status[2], status[3])
        return statuses
    except mysql.connector.Error as e:
        print(e)
        return False
