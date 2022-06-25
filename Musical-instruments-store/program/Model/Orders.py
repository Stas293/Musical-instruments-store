import numpy as np

from program.Model import Status


class Order:
    orderId: int
    dateCreated: str
    login: str
    title: str
    status: Status
    closed: bool = False
    instruments: []

    def __init__(self, order_id, date_created, login, title, status, closed):
        self.orderId = order_id
        self.date_created = date_created
        self.login = login
        self.title = title
        self.status = status
        self.closed = closed

    def getId(self):
        return self.order_id

    def getDateCreated(self):
        return self.date_created

    def setDateCreated(self, date_created):
        self.date_created = date_created

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def setInstruments(self, instruments):
        self.instruments = instruments

    def getInstruments(self):
        return self.instruments

    def printOrder(self):
        print("Order id: " + str(self.orderId))
        print("Date created: " + str(self.date_created))
        print("Login: " + self.login)
        print("Title: " + self.title)
        print("Status: ")
        self.status.printStatus()
        print("Closed: " + str(self.closed))
        print("Instruments: ")
        for instrument in self.instruments:
            instrument.printInstrumentOrder()
