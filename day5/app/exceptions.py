class InvalidCustomerError(ValueError):
    """Raised when the customer input is invalid."""


class CustomerPermissionError(PermissionError):
    """Raised when the user is not allowed to access customer data."""


class OrderFetchError(RuntimeError):
    """Raised when orders cannot be fetched."""