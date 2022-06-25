from program.Model import Status


class OrderDto:
    title: str
    login: str
    status: Status
    def __init__(self, title, login, status):
        self.title = title
        self.login = login
        self.status = status