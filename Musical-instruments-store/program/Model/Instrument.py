from datetime import datetime

from program.Model import Status


class Instrument:
    instrumentId: int
    dateCreated: str
    dateUpdated: str
    description: str
    title: str
    price: float
    isClosed: bool = False
    status: Status

    def __init__(self, description, title, status, price, instrument_id=None, date_created = None, date_updated = None, is_closed = None):
        self.instrumentId = instrument_id
        self.dateCreated = date_created
        self.dateUpdated = date_updated
        self.description = description
        self.title = title
        self.status = status
        self.price = price
        self.isClosed = is_closed

    def getId(self):
        return self.instrumentId

    def getDateCreated(self):
        return self.dateCreated

    def setDateCreated(self, date_created):
        self.dateCreated = date_created

    def getDateUpdated(self):
        return self.dateUpdated

    def setDateUpdated(self):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        self.dateUpdated = formatted_date

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getIsClosed(self):
        return self.isClosed

    def setIsClosed(self, is_closed):
        self.isClosed = is_closed

    def printInstrument(self):
        print("Instrument id: " + str(self.instrumentId))
        print("Title: " + str(self.title))
        print("Description: " + str(self.description))
        print("Date created: " + str(self.dateCreated))
        print("Date updated: " + str(self.dateUpdated))
        print("Status: ")
        self.status.printStatus()
        print("Price: " + str(self.price))
        print("Is closed: " + str(self.isClosed))
