class Account:
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.accountNumber = accountNumber
        self.name = name
        self.age = age
        self.balance = initialBalance
        self.accountType = accountType
        self.status = "Active"

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.accountType

    def getStatus(self):
        return self.status

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age