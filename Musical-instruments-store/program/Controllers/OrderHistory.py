from program.Repository.Order import insert_orderh, get_all_history


# User
def create_orderh(conn, orderHistory):
    insert_orderh(conn, orderHistory)


#Seller
def show_all_history(conn, UDto):
    if get_all_history(conn, UDto) == False:
        print("Error")
        return
    for orderHistory in get_all_history(conn, UDto):
        print("Orders History")
        orderHistory.printOrderHistory()
        print()
