import logging

import frappe

from app.exceptions import (
    InvalidCustomerError,
    OrderFetchError,
)
from app.services import fetch_customer_orders


logger = logging.getLogger(__name__)


@frappe.whitelist()
def get_customer_orders(
    customer: str,
) -> list[dict]:
    """
    Return sales orders for the requested customer.
    """

    if not frappe.has_permission(
        "Sales Order",
        ptype="read",
    ):
        frappe.throw(
            "You do not have permission to view sales orders."
        )

    try:
        return fetch_customer_orders(customer)

    except InvalidCustomerError as error:
        frappe.throw(str(error))

    except OrderFetchError:
        logger.exception(
            "Customer order API failed."
        )

        frappe.throw(
            "Unable to fetch customer orders."
        )