import mysql.connector
import numpy as np

from program.Model import Role


# Admin
def get_role_by_name(roleName, connection):
    try:
        txtSQL = "SELECT * FROM `role` WHERE `name` = %s"
        cursor = connection.cursor()
        cursor.execute(txtSQL, (roleName,))
        role = cursor.fetchone()
        cursor.close()
        role = Role(role[0], role[1], role[2])
        return role
    except mysql.connector.Error as e:
        print(e)
        return False


# Admin
def insert_get_role_for_user(login, connection, roleName):
    try:
        cursor = connection.cursor()
        txtSQL = "SELECT user_id FROM user_list WHERE login = %s"
        cursor.execute(txtSQL, (login,))
        userId = cursor.fetchone()[0]
        role = get_role_by_name(roleName, connection)
        roleId = role.roleId
        textSQL = "INSERT INTO `user_role` (user_id, role_id) VALUES (%s, %s)"
        cursor.execute(textSQL, (userId, roleId))
        connection.commit()
        cursor.close()
        return get_roles_for_user(login, connection)
    except mysql.connector.Error as e:
        print(e)
        return False


# Admin
def get_roles_for_user(login, connection):
    try:
        cursor = connection.cursor()
        textSQL = "select r.* from user_list u join user_role ur on (u.user_id=ur.user_id) left join role r on (ur.role_id=r.role_id) where u.login = %s"
        cursor.execute(textSQL, (login,))
        role = cursor.fetchall()
        cursor.close()
        roles = []
        for r in role:
            ro = Role(r[0], r[1], r[2])
            roles.append(ro)
        return roles
    except mysql.connector.Error as e:
        print(e)
        return False


# Admin
def isInRole(role, conn):
    try:
        cursor = conn.cursor()
        allRoles = cursor.execute("select name from role")
        if role in allRoles:
            return True
        cursor.close()
    except mysql.connector.Error as e:
        print(e)
        return
    return False
