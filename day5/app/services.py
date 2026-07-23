import logging
from typing import Any

from app.exceptions import (
    InvalidCustomerError,
    OrderFetchError,
)
from app.repository import get_orders_by_customer


logger = logging.getLogger(__name__)


def validate_customer(customer: str) -> str:
    """
    Validate and normalize the customer identifier.
    """

    if not isinstance(customer, str):
        raise InvalidCustomerError(
            "Customer must be a string."
        )

    customer = customer.strip()

    if not customer:
        raise InvalidCustomerError(
            "Customer cannot be empty."
        )

    return customer


def fetch_customer_orders(
    customer: str,
) -> list[dict[str, Any]]:
    """
    Fetch all orders for a valid customer.
    """

    customer = validate_customer(customer)

    try:
        orders = get_orders_by_customer(customer)

        logger.info(
            "Fetched %d orders for customer %s",
            len(orders),
            customer,
        )

        return orders

    except Exception as error:
        logger.exception(
            "Failed to fetch orders for customer %s",
            customer,
        )

        raise OrderFetchError(
            "Unable to fetch customer orders."
        ) from error