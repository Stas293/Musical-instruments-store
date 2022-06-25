class Role:
    roleId: int
    code: str
    name: str

    def __init__(self, roleId, code, name):
        self.roleId = roleId
        self.code = code
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def equals(self, code):
        return self.code == code

    def printRole(self):
        print("Role id: " + str(self.roleId))
        print("Role code: " + self.code)
        print("Role name: " + self.name)

