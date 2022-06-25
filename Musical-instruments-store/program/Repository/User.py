from program.Model import User
import mysql.connector


def find_user_by_login(UserD, connection):
    try:
        cursor = connection.cursor()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (UserD.login,))
        user = cursor.fetchone()
        cursor.close()
        if user is None:
            return False
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def insert_user(RegistDto, connection):
    try:
        cursor = connection.cursor()
        textSQL = "INSERT INTO `user_list` (login, first_name, last_name, email, phone, password) VALUES (%s,%s, %s, %s, %s, %s) "
        cursor.execute(textSQL, (RegistDto.login, RegistDto.firstName, RegistDto.lastName, RegistDto.email, RegistDto.phone, RegistDto.password))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (RegistDto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def change_email(Udto, email, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE `user_list` SET email = %s WHERE login = %s"
        cursor.execute(textSQL, (email, Udto.login))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (Udto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def change_first_name(UDto, firstName, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE `user_list` SET first_name = %s WHERE login = %s"
        cursor.execute(textSQL, (firstName, UDto.login))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (UDto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def change_last_name(UDto, lastName, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE `user_list` SET last_name = %s WHERE login = %s"
        cursor.execute(textSQL, (lastName, UDto.login))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (UDto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def change_phone(UDto, phone, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE `user_list` SET phone = %s WHERE login = %s"
        cursor.execute(textSQL, (phone, UDto.login))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (UDto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def change_password(UDto, password, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE `user_list` SET password = %s WHERE login = %s"
        cursor.execute(textSQL, (password, UDto.login))
        connection.commit()
        txtSQL = "SELECT * FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (UDto.login,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


# Admin
def disable_u(UDto, connection):
    try:
        cursor = connection.cursor()
        textSQL = "UPDATE user_list SET enabled = 0 WHERE login = %s"
        cursor.execute(textSQL, (UDto.login,))
        connection.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        return False


def get_user_by_id(connection, id):
    try:
        cursor = connection.cursor()
        textSQL = "SELECT * FROM user_list WHERE user_id = %s"
        cursor.execute(textSQL, (id,))
        user = cursor.fetchone()
        cursor.close()
        new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
        return new_user
    except mysql.connector.Error as e:
        print(e)
        return None


def all_users(db):
    try:
        cursor = db.cursor()
        textSQL = "SELECT * FROM user_list"
        cursor.execute(textSQL)
        users = cursor.fetchall()
        cursor.close()
        userss = []
        for user in users:
            new_user = User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8])
            userss.append(new_user)
        return userss
    except mysql.connector.Error as e:
        print(e)
        return None