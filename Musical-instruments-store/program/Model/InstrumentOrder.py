from program.Model import Instrument


class InstrumentOrder:
    instrument: Instrument
    price: int
    quantity: int

    def __init__(self, instrument, price, quantity):
        self.instrument = instrument
        self.price = price
        self.quantity = quantity

    def getInstruments(self):
        return self.instrument

    def setInstruments(self, instrument):
        self.instrument = instrument

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getQuantity(self):
        return self.quantity

    def printInstrumentOrder(self):
        self.instrument.printInstrument()
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))

