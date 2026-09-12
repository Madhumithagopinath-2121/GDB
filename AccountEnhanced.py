from abc import ABC, abstractmethod

from AccountException import AccountException
from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import MinimumBalanceViolationException
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException


class Account(ABC):

    # Constants
    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999

    # Abstract methods
    @abstractmethod
    def getMinimumBalance(self):
        pass

    @abstractmethod
    def getAccountType(self):
        pass

    # Constructor
    def __init__(self, accountNumber, name, age, initialBalance):

        # Age validation
        if age < self.MIN_AGE:
            raise ValueError(
                "Customer must be at least "
                + str(self.MIN_AGE)
                + " years old. Provided: "
                + str(age)
            )

        # Minimum balance validation
        minimum_balance = self.getMinimumBalance()

        if initialBalance < minimum_balance:
            raise ValueError(
                self.getAccountType()
                + " account requires minimum balance of ₹"
                + str(minimum_balance)
                + ". Provided: ₹"
                + str(initialBalance)
            )

        # Common fields
        self.accountNumber = accountNumber
        self.name = name
        self.age = age
        self.balance = initialBalance
        self.status = "Active"
        self.pin = None

    # ===== Helper Methods =====

    def validateActive(self):

        if self.status != "Active":
            raise InactiveAccountException(
                "Account is inactive"
            )

    def validateAmount(self, amount):

        if amount <= 0:
            raise InvalidAmountException(
                "Amount must be greater than zero"
            )

    def validatePin(self, pin):

        if self.pin is None:
            raise InvalidPinException(
                "PIN is not set"
            )

        if not self.verifyPin(pin):
            raise InvalidPinException(
                "Invalid PIN"
            )

    # ===== Deposit =====

    def deposit(self, amount):

        self.validateActive()

        self.validateAmount(amount)

        self.balance += amount

    # ===== Withdraw =====

    def withdraw(self, amount, pin):

        self.validateActive()

        self.validatePin(pin)

        self.validateAmount(amount)

        if amount > self.balance:
            raise InsufficientBalanceException(
                "Insufficient balance"
            )

        minimum_balance = self.getMinimumBalance()

        if self.balance - amount < minimum_balance:
            raise MinimumBalanceViolationException(
                "Withdrawal would violate minimum balance of ₹"
                + str(minimum_balance)
            )

        self.balance -= amount

    # ===== Account Status =====

    def closeAccount(self):

        if self.status == "Inactive":
            raise RuntimeError(
                "Account is already closed"
            )

        self.status = "Inactive"

    def reopenAccount(self):

        if self.status == "Active":
            raise RuntimeError(
                "Account is already active"
            )

        self.status = "Active"

    # ===== PIN Management =====

    def setPin(self, pin):

        if pin < self.MIN_PIN or pin > self.MAX_PIN:
            raise ValueError(
                "PIN must be a 4-digit number"
            )

        self.pin = pin

    def verifyPin(self, pin):

        if self.pin is None:
            return False

        return self.pin == pin

    def hasPin(self):

        return self.pin is not None

    # ===== Balance Helper =====

    def setBalance(self, balance):
        self.balance = balance

    # ===== Getters =====

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getStatus(self):
        return self.status

    # ===== Setters =====

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age