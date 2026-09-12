from AccountEnhanced import Account
from InsufficientBalanceException import InsufficientBalanceException


class CurrentAccount(Account):

    # Constants
    MINIMUM_BALANCE = 1000.0
    ACCOUNT_TYPE = "Current"
    OVERDRAFT_LIMIT = 5000.0

    def __init__(self, accountNumber, name, age, initialBalance):
        super().__init__(
            accountNumber,
            name,
            age,
            initialBalance
        )

        self.overdraftUsed = 0.0

    def getMinimumBalance(self):
        return self.MINIMUM_BALANCE

    def getAccountType(self):
        return self.ACCOUNT_TYPE

    # ===== Overdraft Withdrawal =====

    def withdraw(self, amount, pin):

        self.validateActive()
        self.validatePin(pin)
        self.validateAmount(amount)

        availableBalance = (
            self.balance
            - self.MINIMUM_BALANCE
            + self.OVERDRAFT_LIMIT
            - self.overdraftUsed
        )

        if amount > availableBalance:
            raise InsufficientBalanceException(
                "Insufficient balance. Available funds: ₹"
                + str(availableBalance)
            )

        newBalance = self.balance - amount

        # Calculate overdraft used
        if newBalance < self.MINIMUM_BALANCE:
            overdraftAmount = (
                self.MINIMUM_BALANCE - newBalance
            )

            self.overdraftUsed += overdraftAmount

        self.setBalance(newBalance)

    # ===== Overdraft Methods =====

    def getOverdraftLimit(self):
        return self.OVERDRAFT_LIMIT

    def getOverdraftUsed(self):
        return self.overdraftUsed

    def getAvailableOverdraft(self):
        return (
            self.OVERDRAFT_LIMIT
            - self.overdraftUsed
        )

    def isUsingOverdraft(self):
        return self.overdraftUsed > 0

    def repayOverdraft(self, amount):

        self.validateAmount(amount)

        if amount > self.overdraftUsed:
            amount = self.overdraftUsed

        self.balance += amount
        self.overdraftUsed -= amount