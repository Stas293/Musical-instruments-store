from program.Controllers.AMUser import login, sign_up
from program.Controllers.ViewAddInstruments import get_number_of_instruments, get_instrument_by_page, \
    show_all_instuments


def choice():
    while True:
        print('Log in (1) or sign up (2) or show instruments (3) or exit (0)?')
        num = input('Please enter number: ')
        if num in ['1', '2', '3', '0']:
            return num
        else:
            print("Not a valid number. Please try again.")


def enter_app(db):
    num = choice()
    if num == '1':
        user, UserD = login(db)
        return user, UserD
    elif num == '2':
        user, UserD = sign_up(db)
        return user, UserD
    elif num == '3':
        if get_number_of_instruments(db) > 2:
            t = True
            while t:
                print("Enter page: ")
                page = int(input())
                get_instrument_by_page(db, page)
                print("Choose page? (y/n): ")
                proceed = input()
                if proceed == "y":
                    t = True
                else:
                    t = False
        else:
            show_all_instuments(db)
        return 1, None
    elif num == '0':
        print("Bye!")
        return None, None


