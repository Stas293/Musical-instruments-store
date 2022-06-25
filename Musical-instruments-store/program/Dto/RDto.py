

class RDto:
    login: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str

    def __init__(self, login, firstName, lastName, email, password, phone):
        self.login = login
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
