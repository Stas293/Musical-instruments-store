from datetime import datetime


class User:
    userId: int
    login: str
    firstName: str
    lastName: str
    email: str
    phone: str
    password: str
    enable: bool = True
    dateCreated: str
    dateModified: str
    roles = []

    def __init__(self, userId, login, firstName, lastName, email, phone, password, dateCreated, dateModified):
        self.userId = userId
        self.login = login
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.password = password
        self.dateCreated = dateCreated
        self.dateModified = dateModified

    def getId(self):
        return self.userId

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getFullName(self):
        return self.firstName + self.lastName

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def isEnabled(self):
        return self.enable

    def getRoles(self):
        return self.roles

    def setRoles(self, roles):
        self.roles = roles

    def getDateCreated(self):
        return self.dateCreated

    def getDateModified(self):
        return self.dateModified

    def setDateModified(self):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        self.dateModified = formatted_date

    def printUser(self):
        print("User id: " + str(self.userId))
        print("Login: " + self.login)
        print("First name: " + self.firstName)
