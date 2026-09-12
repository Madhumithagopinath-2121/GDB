from AccountException import AccountException


class InvalidPinException(AccountException):

    def __init__(self, message):
        super().__init__(message)