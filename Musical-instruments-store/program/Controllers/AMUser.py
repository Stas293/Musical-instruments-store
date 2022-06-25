import hashlib

from program.Dto import UDto, RDto
from program.Repository.Role import get_roles_for_user, insert_get_role_for_user
from program.Repository.User import find_user_by_login, insert_user, change_email, change_first_name, change_last_name, \
    change_phone, change_password, disable_u, all_users


# All users
def login(conn):
    print("Login: ")
    loginn = input()
    loginn = loginn.strip()
    print("Password: ")
    password = input()
    password = password.strip()
    password = hashlib.sha256((loginn + password).encode()).hexdigest()

    UserD = UDto(loginn)
    user = find_user_by_login(UserD, conn)

    if user is not None:
        if password == user.password:
            if not user.enable:
                print('Your account is disabled.')
                return None, None
            print('You were successfully logged in')
            roles = get_roles_for_user(loginn, conn)
            user.setRoles(roles)
            for role in roles:
                print(role.name)
            print("Welcome")
            user.printUser()
            print()
            return user, UserD
        else:
            print('Not correct')
            return None, None
    else:
        print('User not found')
        return 1, None


# All users
def sign_up(conn):
    print("Login: ")
    login = input()
    login = login.strip()
    print("Email: ")
    email = input()
    email = email.strip()
    print("First name: ")
    firstName = input()
    firstName = firstName.strip()
    print("Last name: ")
    lastName = input()
    lastName = lastName.strip()
    print("Phone: ")
    phone = input()
    phone = phone.strip()
    print("Password: ")
    password1 = input()
    password1 = password1.strip()
    print("Confirm password: ")
    password2 = input()
    password2 = password2.strip()

    password = hashlib.sha256((login + password1).encode()).hexdigest()

    user = find_user_by_login(UDto(login), conn)

    RegDto = RDto(login, firstName, lastName, email, password, phone)

    if user:
        print('User already exists')
        return None, None
    elif len(login) < 3:
        print('Login must be greater than 3 characters.')
        return None, None
    elif len(email) < 5:
        print('Email must be greater than 5 characters.')
        return None, None
    elif len(firstName) < 3:
        print('First name must be greater than 3 characters.')
        return None, None
    elif len(lastName) < 3:
        print('Last name must be greater than 3 characters.')
        return None, None
    elif len(phone) != 13:
        print('Phone must be 13 characters in length.')
        return None, None
    elif password1 != password2:
        print('Passwords don\'t match.')
        return None, None
    elif len(password1) < 7:
        print('Password must be at least 7 characters.')
        return None, None
    else:
        new_user = insert_user(RegDto, conn)
        role = insert_get_role_for_user(RegDto.login, conn, 'User')
        new_user.setRoles(role)
        print('Account created!')
        print("Welcome")
        new_user.printUser()
        return new_user, UDto(new_user.login)


# User
def modify_user(conn, UDto):
    print("What do you want to change?")
    print("1. Email")
    print("2. First name")
    print("3. Last name")
    print("4. Phone")
    print("5. Password")
    c = int(input())
    if c == 1:
        print("New email: ")
        email = input()
        email = email.strip()
        user = change_email(UDto, email, conn)
        if user is False:
            print('Email is already in use or is invalid.')
            user = find_user_by_login(UDto, conn)
        roles = get_roles_for_user(UDto.login, conn)
        user.setRoles(roles)
        return user, UDto
    elif c == 2:
        print("New first name: ")
        firstName = input()
        firstName = firstName.strip()
        user = change_first_name(UDto, firstName, conn)
        if user is False:
            print("We can't change first name to this value. Try again later.")
            user = find_user_by_login(UDto, conn)
        roles = get_roles_for_user(UDto.login, conn)
        user.setRoles(roles)
        return user, UDto
    elif c == 3:
        print("New last name: ")
        lastName = input()
        lastName = lastName.strip()
        user = change_last_name(UDto, lastName, conn)
        if user is False:
            print("We can't change last name to this value. Try again later.")
            user = find_user_by_login(UDto, conn)
        roles = get_roles_for_user(UDto.login, conn)
        user.setRoles(roles)
        return user, UDto
    elif c == 4:
        print("New phone: ")
        phone = input()
        phone = phone.strip()
        user = change_phone(UDto, phone, conn)
        if user is False:
            print("We can't change phone to this value. Try again later.")
            user = find_user_by_login(UDto, conn)
        roles = get_roles_for_user(UDto.login, conn)
        user.setRoles(roles)
        return user, UDto
    elif c == 5:
        print("New password: ")
        password = input()
        password = password.strip()
        password = hashlib.sha256((UDto.login + password).encode()).hexdigest()
        user = change_password(UDto, password, conn)
        if user is False:
            print("We can't change password to this value. Try again later.")
            user = find_user_by_login(UDto, conn)
        roles = get_roles_for_user(UDto.login, conn)
        user.setRoles(roles)
        return user, UDto
    else:
        print("Wrong choice")
        return


# Admin
def disable_user(conn):
    print("Choose user: ")
    users = all_users(conn)
    for u in users:
        print(u.login)
    print()
    print("Login: ")
    login = input()
    login = login.strip()
    user = find_user_by_login(UDto(login), conn)
    if user:
        if not user.enable:
            print(login + ' account is already disabled.')
            return
        disable_u(UDto(login), conn)
        print(login + ' account is disabled.')
    else:
        print('User not found')
        return


# Admin
def add_role_for_user(db):
    print("Choose user: ")
    users = all_users(db)
    for u in users:
        print(u.login)
    print()
    print("Login: ")
    login = input()
    user = find_user_by_login(UDto(login), db)
    if user is not None:
        print("Role: ")
        role = input()
        insert_get_role_for_user(login, db, role)
        print(login + ' account is added to ' + role + ' role.')
    else:
        print('User not found')
        return

