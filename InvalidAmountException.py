from AccountException import AccountException


class InvalidAmountException(AccountException):

    def __init__(self, message):
        super().__init__(message)