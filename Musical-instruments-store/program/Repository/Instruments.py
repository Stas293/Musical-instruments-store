import numpy as np
import mysql.connector
from program.Model import Instrument


# User
from program.Repository.Status import find_status_by_id


def number_of_instruments(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM instrument_list")
        number = cursor.fetchone()
        cursor.close()
        return number[0]
    except mysql.connector.Error as e:
        print(e)
        return False


# User
def get_all_instruments(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM instrument_list")
        instruments = cursor.fetchall()
        cursor.close()
        instrument = []
        for i in instruments:
            status = find_status_by_id(i[5], conn)
            inst = Instrument(i[3], i[4], status, i[6], i[0], i[1], i[2], i[7])
            instrument.append(inst)
        return instrument
    except mysql.connector.Error as e:
        print(e)
        return False


# User
def instrument_from_by(conn, begin, end):
    try:
        cursor = conn.cursor()
        textSQL = "SELECT * FROM instrument_list limit %s offset %s"
        cursor.execute(textSQL, (end-begin, begin))
        instruments = cursor.fetchall()
        cursor.close()
        instrument = []
        for i in instruments:
            status = find_status_by_id(i[5], conn)
            inst = Instrument(i[3], i[4], status, i[6], i[0], i[1], i[2], i[7])
            instrument.append(inst)
        return instrument
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def insert_instrument(instrument, conn):
    try:
        cursor = conn.cursor()
        textSQL = "INSERT INTO instrument_list (description, title, status_id, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(textSQL, (instrument.description, instrument.title, instrument.status.statusId, instrument.price))
        conn.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        return False

