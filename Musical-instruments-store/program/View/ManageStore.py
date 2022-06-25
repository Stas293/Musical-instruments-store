from program.Controllers.AMUser import modify_user, disable_user, add_role_for_user
from program.Controllers.MakeOrders import make_order, view_orders, view_all_orders, change_status_order
from program.Controllers.OrderHistory import show_all_history
from program.Controllers.Status import add_status, get_statuses, update_status_by_name
from program.Controllers.ViewAddInstruments import show_all_instuments, get_number_of_instruments, add_instrument, \
    find_instrument_by_title


def choice(roles):
    while True:
        if 'User' in roles:
            print("Modify profile (1)")
            print("Make order (2)")
            print("View orders (3)")
            print("View all instruments (4)")
            print("Find instrument by title (5)")
            print("Show history orders (6)")

        if 'Seller' in roles:
            print("View orders (7)")
            print("View all orders (8)")
            print("Change status of order (9)")
            print("Get statuses (10)")
            print("Get number of instruments (11)")
            print("Add instrument (12)")

        if 'Admin' in roles:
            print("Disable user (13)")
            print("Add status (14)")
            print("Add role for user (15)")

        print("Exit (0)")
        print("Logout (16)")
        print("Enter your choice: ")
        choic = int(input())
        if 0 < choic < 7 and ('User' not in roles):
            print("You are not a user")
            continue
        if 6 < choic < 13 and ('Seller' not in roles):
            print("Wrong number")
            continue
        if 12 < choic < 16 and ('Admin' not in roles):
            print("You are not an admin")
            continue
        if choic in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            return choic
        else:
            print("Not a valid number. Please try again.")


def work_app(db, roles, UDto):
    num = choice(roles)
    while num != 0:
        if num == 1:
            print()
            modify_user(db, UDto)
            print()
        elif num == 2:
            print()
            make_order(db, UDto)
            print()
        elif num == 3:
            print()
            view_orders(db, UDto)
            print()
        elif num == 4:
            print()
            show_all_instuments(db)
            print()
        elif num == 5:
            print()
            print("Enter title: ")
            title = input()
            if find_instrument_by_title(db, title) is not None:
                find_instrument_by_title(db, title).printInstrument()
            print()
        elif num == 6:
            print()
            show_all_history(db, UDto)
            print()
        elif num == 7:
            print()
            view_orders(db, UDto)
            print()
        elif num == 8:
            print()
            view_all_orders(db)
            print()
        elif num == 9:
            print()
            change_status_order(db)
            print()
        elif num == 10:
            print()
            get_statuses(db)
            print()
        elif num == 11:
            print()
            print("Number of instruments: " + str(get_number_of_instruments(db)))
            print()
        elif num == 12:
            print()
            add_instrument(db)
            print()
        elif num == 13:
            print()
            disable_user(db)
            print()
        elif num == 14:
            print()
            add_status(db)
            print()
        elif num == 15:
            print()
            add_role_for_user(db)
            print()
        elif num == 16:
            print()
            return 1
        num = choice(roles)
    print("Bye!")
    return False
