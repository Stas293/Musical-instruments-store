import random

from program.Model import Status
from program.Repository.Status import insert_status, find_all_statuses, find_status_by_name, update_status, \
    possible_stat


# Admin
def add_status(conn):
    code = input("Enter code: ")
    name = input("Enter name: ")
    is_closed = input("Is closed? (y/n): ")
    if is_closed == "y":
        is_closed = True
    else:
        is_closed = False
    print("Proceed? (y/n): ")
    proceed = input()
    if proceed == "y":
        statusId = random.randint(1, 100)
        status = Status(statusId, code, name, is_closed)
        s = insert_status(status, conn)
        if s == False:
            print("Status error")
            return
    else:
        print("Canceled")


# Seller
def find_by_name(conn, name):
    status = find_status_by_name(name, conn)
    if status == False:
        print("Status error")
        return
    elif status == None:
        print("Status not found")
        return
    return status


# Seller
def get_statuses(conn):
    for status in find_all_statuses(conn):
        status.printStatus()
        print()


# Admin
def update_status_by_name(conn):
    print("Enter name of status to update: ")
    name1 = input()
    name = input("Enter name: ")
    code = input("Enter code: ")
    is_closed = input("Is closed? (y/n): ")
    if is_closed == "y":
        is_closed = True
    else:
        is_closed = False
    statusId = random.randint(1, 100)
    status = Status(statusId, code, name, is_closed)
    update_status(status, conn, name1)


# Seller
def possible_status(conn, status):
    next_status = possible_stat(status, conn)
    print("Next status: ")
    next_status.printStatus()
    print("Proceed? (y/n): ")
    proceed = input()
    if proceed == "y":
        return next_status
    else:
        return status
