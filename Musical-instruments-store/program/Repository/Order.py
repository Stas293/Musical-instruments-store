import numpy as np
import mysql.connector
from program.Model import Status, InstrumentOrder, Instrument, OrderHistory, User
from program.Model.Orders import Order


# User
from program.Repository.User import get_user_by_id


def insert_order(conn, order):
    try:
        order1 = order
        cur = conn.cursor()
        textSQL = "SELECT user_id FROM user_list WHERE login = %s"
        cur.execute(textSQL, (order.login,))
        userId = cur.fetchone()[0]
        textSQL = "SELECT status_id FROM status WHERE name = %s"
        cur.execute(textSQL, (order.status.name,))
        statusId = cur.fetchone()[0]
        textSQL = "INSERT INTO order_list (title, user_id, status_id) VALUES (%s, %s, %s)"
        cur.execute(textSQL, (order.title, userId, statusId))
        conn.commit()
        textSQL = "SELECT * FROM order_list WHERE user_id = %s order by date_created desc limit 1"
        cur.execute(textSQL, (userId,))
        order = cur.fetchone()
        cur.close()
        return Order(order[0], order[1], order1.login, order[3], order1.status, order[5])
    except mysql.connector.Error as e:
        print(e)
        return False


# User, Seller
def get_orders(conn, UDto):
    try:
        cur = conn.cursor()
        textSQL = "SELECT user_id FROM user_list WHERE login = %s"
        cur.execute(textSQL, (UDto.login,))
        userId = cur.fetchone()[0]
        textSQL = "SELECT * FROM order_list WHERE user_id = %s order by date_created"
        cur.execute(textSQL, (userId,))
        orders = cur.fetchall()
        order = []
        for i in orders:
            textSQL = "SELECT * FROM status WHERE status_id = %s"
            cur.execute(textSQL, (i[4],))
            status = cur.fetchone()
            statuss = Status(status[0], status[1], status[2], status[3])
            textSQL = "SELECT * FROM instrument_order WHERE order_id = %s"
            cur.execute(textSQL, (i[0],))
            instruments = cur.fetchall()
            instruments_list = []
            for j in instruments:
                textSQL = "SELECT * FROM instrument_list WHERE instrument_id = %s"
                cur.execute(textSQL, (j[0],))
                instrument = cur.fetchone()
                textSQL = "SELECT * FROM status WHERE status_id = %s"
                cur.execute(textSQL, (instrument[5],))
                statusss = cur.fetchone()
                statussss = Status(statusss[0], statusss[1], statusss[2], statusss[3])
                instruments_list.append(InstrumentOrder(Instrument(instrument[3], instrument[4], statussss, instrument[6], instrument[0], instrument[1] , instrument[2], instrument[7]), j[2], j[3]))
            ord = Order(i[0], i[1], UDto.login, i[3], statuss, i[5])
            ord.instruments = instruments_list
            order.append(ord)
        cur.close()
        return order
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def get_all_users(conn):
    try:
        cur = conn.cursor()
        textSQL = "SELECT user_id FROM user_list"
        cur.execute(textSQL)
        users = cur.fetchall()
        cur.close()
        user = []
        for i in users:
            user.append(get_user_by_id(conn, i[0]))
        return user
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def get_order_status(conn, orderId):
    try:
        cur = conn.cursor()
        textSQL = "SELECT status_id FROM order_list WHERE order_id = %s"
        cur.execute(textSQL, (orderId,))
        statusId = cur.fetchone()[0]
        textSQL = "SELECT * FROM status WHERE status_id = %s"
        cur.execute(textSQL, (statusId,))
        status = cur.fetchone()
        cur.close()
        return Status(status[0], status[1], status[2], status[3])
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def update_order_status(conn, order_id, next_status):
    try:
        cur = conn.cursor()
        textSQL = "SELECT status_id FROM status WHERE name = %s"
        cur.execute(textSQL, (next_status.name,))
        statusId = cur.fetchone()[0]
        textSQL = "UPDATE order_list SET status_id = %s WHERE order_id = %s"
        cur.execute(textSQL, (statusId, order_id))
        conn.commit()
        cur.close()
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def get_order_by_id(conn, orderId):
    try:
        cur = conn.cursor()
        textSQL = "SELECT * FROM order_list WHERE order_id = %s"
        cur.execute(textSQL, (orderId,))
        order = cur.fetchone()
        if order is None:
            return False
        textSQL = "SELECT * FROM status WHERE status_id = %s"
        cur.execute(textSQL, (order[4],))
        status = cur.fetchone()
        textSQL = "SELECT login FROM user_list WHERE user_id = %s"
        cur.execute(textSQL, (order[2],))
        login = cur.fetchone()[0]
        cur.close()
        return Order(order[0], order[1], login, order[3], Status(status[0], status[1], status[2], status[3]), order[5])
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def get_total_sum(conn, orderId):
    try:
        cur = conn.cursor()
        textSQL = "SELECT * FROM instrument_order WHERE order_id = %s"
        cur.execute(textSQL, (orderId,))
        instruments = cur.fetchall()
        total_sum = 0
        for i in instruments:
            total_sum += i[2] * i[3]
        cur.close()
        return total_sum
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def insert_orderh(conn, orderHistory):
    try:
        cur = conn.cursor()
        textSQL = "INSERT INTO order_history (user_id, total_sum, title, status_id) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(textSQL, (orderHistory.user.userId, orderHistory.totalSum, orderHistory.title, orderHistory.status.statusId))
        conn.commit()
        cur.close()
    except mysql.connector.Error as e:
        print(e)
        return False


# Seller
def delete_order(conn, order_id):
    try:
        cur = conn.cursor()
        textSQL = "DELETE FROM order_list WHERE order_id = %s"
        cur.execute(textSQL, (order_id,))
        conn.commit()
        cur.close()
    except mysql.connector.Error as e:
        print(e)
        return False


def get_all_history(conn, UDto):
    try:
        cur = conn.cursor()
        textSQL = "SELECT * FROM user_list WHERE login = %s"
        cur.execute(textSQL, (UDto.login,))
        user = cur.fetchone()
        textSQL = "SELECT * FROM order_history WHERE user_id = %s order by date_created"
        cur.execute(textSQL, (user[0],))
        orders = cur.fetchall()
        order = []
        for i in orders:
            textSQL = "SELECT * FROM status WHERE status_id = %s"
            cur.execute(textSQL, (i[6],))
            status = cur.fetchone()
            statuss = Status(status[0], status[1], status[2], status[3])
            order.append(OrderHistory(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[8], user[9]), i[3], i[4], statuss, i[0], i[1]))
        cur.close()
        return order
    except mysql.connector.Error as e:
        print(e)
        return False
