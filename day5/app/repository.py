from typing import Any


ORDERS: list[dict[str, Any]] = [
    {
        "name": "SO-001",
        "customer": "CUST-001",
        "grand_total": 1000,
    },
    {
        "name": "SO-002",
        "customer": "CUST-001",
        "grand_total": 2500,
    },
    {
        "name": "SO-003",
        "customer": "CUST-002",
        "grand_total": 1500,
    },
]


def get_orders_by_customer(
    customer: str,
) -> list[dict[str, Any]]:
    """
    Return all orders belonging to the given customer.
    """

    return [
        order
        for order in ORDERS
        if order["customer"] == customer
    ]