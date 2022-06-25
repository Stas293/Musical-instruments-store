from program.Controllers.Status import get_statuses, find_by_name
from program.Model import Status, Instrument
from program.Repository.Instruments import number_of_instruments, instrument_from_by, insert_instrument, \
    get_all_instruments


# User
def show_all_instuments(conn):
    for instrument in get_all_instruments(conn):
        instrument.printInstrument()
        print()


# Seller
def get_number_of_instruments(conn):
    return number_of_instruments(conn)


# User
def get_instrument_by_page(conn, page):
    num_instr = 2
    if (float(get_number_of_instruments(conn))-num_instr*(page-1)) < 0:
        print("Page not found")
        return
    begin = (page - 1) * num_instr
    end = begin + num_instr
    for instrument in instrument_from_by(conn, begin, end):
        instrument.printInstrument()
        print()


# Seller
def add_instrument(conn):
    print("Enter title: ")
    title = input()
    title = title.capitalize()
    title = title.strip()
    print("Enter description: ")
    description = input()
    print("Possible statuses: ")
    get_statuses(conn)
    print("Choose name of the status: ")
    name = input()
    statuss = find_by_name(conn, name)
    print("Enter price: ")
    price = int(input())
    instrument = Instrument(title = title, description = description, status = statuss, price = price)
    insert_instrument(instrument, conn)


# User
def find_instrument_by_title(conn, title):
    title = title.capitalize()
    title = title.strip()
    for instrument in get_all_instruments(conn):
        if instrument.title == title:
            return instrument
    print("Instrument not found")
    return None
