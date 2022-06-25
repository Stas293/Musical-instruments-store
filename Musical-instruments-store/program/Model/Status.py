
class Status:
    statusId: int
    code: str
    name: str
    isClosed: bool = False

    def __init__(self, statusId, code, name, is_closed):
        self.statusId = statusId
        self.code = code
        self.name = name
        self.isClosed = is_closed

    def getId(self):
        return self.id

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getClosed(self):
        return self.isClosed

    def setClosed(self, closed):
        self.isClosed = closed

    def getId(self):
        return self.id

    def printStatus(self):
        print("Status id: " + str(self.statusId))
        print("Status code: " + self.code)
        print("Status name: " + self.name)
        print("Status isClosed: " + str(self.isClosed))
