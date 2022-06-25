from program.Controllers.InstrumentOrders import make_instrument_orders
from program.Controllers.OrderHistory import create_orderh
from program.Controllers.Status import find_by_name, possible_status
from program.Dto import UDto
from program.Dto.OrderDto import OrderDto
from program.Model import InstrumentOrder, OrderHistory
from program.Model.Orders import Order
from program.Repository.Order import insert_order, get_orders, get_all_users, get_order_status, update_order_status, \
    get_total_sum, get_order_by_id, delete_order

from program.Repository.User import find_user_by_login


# User
def make_order(conn, UDto):
    print("Enter title of the order: ")
    title = input()
    title = title.strip()
    title = title.capitalize()
    status = find_by_name(conn, "Not processed")
    if status is False:
        print("Status error")
        return
    order = OrderDto(title = title, login = UDto.login, status = status)
    order = insert_order(conn, order)
    if order is False:
        print("Order error")
        return
    instruments = []
    t = True
    while t:
        print("Proceed with adding instruments? (y/n): ")
        proceed = input()
        if proceed == "y":
            instruments.append(make_instrument_orders(conn, order))
            print("Add another instrument? (y/n): ")
            proceed = input()
            if proceed == "y":
                t = True
            else:
                t = False
        else:
            t = False
    order.setInstruments(instruments)
    return order


# User, Seller
def view_orders(conn, UDto):
    print("Order: ")
    if get_orders(conn, UDto) == False:
        print("Orders error")
        return
    for order in get_orders(conn, UDto):
        order.printOrder()


# Seller
def view_all_orders(conn):
    print("Orders: ")
    if get_all_users(conn) == False:
        print("Orders error")
        return
    for user in get_all_users(conn):
        print("User: " + user.login)
        view_orders(conn, UDto(user.login))
        print()


# Seller
def change_status_order(conn):
    view_all_orders(conn)
    if view_all_orders(conn) == False:
        print("Orders error")
        return
    print("Enter user login: ")
    login = input()
    if find_user_by_login(UDto(login), conn) == False:
        print("User not found")
        return
    print("Enter order id: ")
    order_id = int(input())
    if get_order_by_id(conn, order_id) == False or get_order_by_id(conn, order_id).login != login:
        print("Order not found")
        return
    ords = get_order_status(conn, order_id)
    if ords == False:
        print("Orders error")
        return
    next_status = possible_status(conn, ords)
    if next_status == False:
        print("Status error")
        return
    update_order_status(conn, order_id, next_status)
    view_orders(conn, UDto(login))
    if next_status.name == "Received":
        print("Order is received")
        create_orderh(conn, OrderHistory(user = find_user_by_login(UDto(login), conn),
                                         total_sum = get_total_sum(conn, order_id),
                                         title = get_order_by_id(conn, order_id).title, status = next_status))
        delete_order(conn, order_id)
