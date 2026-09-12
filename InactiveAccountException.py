from AccountException import AccountException


class InactiveAccountException(AccountException):

    def __init__(self, message):
        super().__init__(message)