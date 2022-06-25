import mysql.connector


def insert_instrument_order(conn, instrumentOrd, order):
    try:
        cur = conn.cursor()
        textSQL = "INSERT INTO instrument_order (instrument_id, order_id, price, quantity) VALUES (%s, %s, %s, %s)"
        cur.execute(textSQL,
                    (instrumentOrd.instrument.instrumentId, order.orderId, instrumentOrd.price, instrumentOrd.quantity))
        textSQL = "SELECT closed FROM instrument_list where instrument_id = %s"
        cur.execute(textSQL, (instrumentOrd.instrument.instrumentId,))
        closed = cur.fetchone()[0]
        if closed == 1:
            conn.rollback()
            cur.close()
            return False
        conn.commit()
        cur.close()
    except mysql.connector.Error as e:
        print(e)
        return False
