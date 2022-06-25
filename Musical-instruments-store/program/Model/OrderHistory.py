from program.Model import User, Status


class OrderHistory:
    historyId: int
    dateCreated: str
    user: User
    totalSum: float
    title: str
    status: Status

    def __init__(self, user, total_sum, title, status, historyId = None, date_created = None):
        self.historyId = historyId
        self.dateCreated = date_created
        self.user = user
        self.totalSum = total_sum
        self.title = title
        self.status = status

    def getId(self):
        return self.historyId

    def getDateCreated(self):
        return self.dateCreated

    def setDateCreated(self, date_created):
        self.dateCreated = date_created

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

    def getTotalSum(self):
        return self.totalSum

    def setTotalSum(self, total_sum):
        self.totalSum = total_sum

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

