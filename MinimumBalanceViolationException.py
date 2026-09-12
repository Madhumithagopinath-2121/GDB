from AccountException import AccountException


class MinimumBalanceViolationException(AccountException):

    def __init__(self, message):
        super().__init__(message)