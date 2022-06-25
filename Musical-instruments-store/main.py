import os
import mysql.connector
from dotenv import load_dotenv, find_dotenv

from program.Dto import UDto
from program.View.Login import enter_app
from program.View.ManageStore import work_app

load_dotenv(find_dotenv())

DB_NAME = os.getenv('DB_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')


def get_roles(user):
    roles = []
    for r in user.roles:
        roles.append(r.name)
    return roles


def create_app():
    try:
        db = mysql.connector.connect(
            host = HOST,
            user = 'root',
            password = PASSWORD,
            database = DB_NAME
        )
    except mysql.connector.Error as e:
        print(e)
        return

    t = True
    while t:
        user, UserD = enter_app(db)
        if user == 1:
            return 1
        elif user is not None:
            while t:
                roles = get_roles(user)
                t = work_app(db, roles, UDto = UDto(user.login))
                if t == 1:
                    break
        elif user is None:
            t = False
    db.close()


t = True

while t:
    t = create_app()
