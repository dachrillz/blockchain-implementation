class InvalidTransactionError(Exception):
    def __init__(self, message, errors=None):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        self.errors = errors
