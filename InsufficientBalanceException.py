from AccountException import AccountException


class InsufficientBalanceException(AccountException):

    def __init__(self, message):
        super().__init__(message)