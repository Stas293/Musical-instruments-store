from program.Controllers.ViewAddInstruments import get_number_of_instruments, get_instrument_by_page, \
    show_all_instuments, find_instrument_by_title
from program.Model import InstrumentOrder, Instrument
from program.Repository.InstrumentsOrder import insert_instrument_order


# User
def make_instrument_orders(conn, order):
    n = get_number_of_instruments(conn)
    if n > 5:
        get_instrument_by_page(conn, 1)
        print("Next? (y/n): ")
        proceed = input()
        if proceed == "y":
            t = True
        else:
            t = False
        while t:
            print("Enter page: ")
            page = int(input())
            get_instrument_by_page(conn, page)
            print("Choose page? (y/n): ")
            proceed = input()
            if proceed == "y":
                t = True
            else:
                t = False
    else:
        show_all_instuments(conn)
    print("Choose instrument(title): ")
    title = input()
    title = title.strip()
    title = title.capitalize()
    instrument = find_instrument_by_title(conn, title)
    if instrument is None or instrument is False:
        print("Instrument not found")
    elif instrument.isClosed:
        print("Instrument is closed")
    else:
        print("Enter quantity: ")
        quantity = int(input())
        instrumentO = InstrumentOrder(instrument, instrument.price, quantity)
        insert_instrument_order(conn, instrumentO, order)
        return instrumentO
