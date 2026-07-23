from unittest.mock import patch

import pytest

from app.exceptions import (
    InvalidCustomerError,
    OrderFetchError,
)
from app.services import (
    fetch_customer_orders,
    validate_customer,
)


def test_validate_customer_accepts_valid_customer():
    result = validate_customer("CUST-001")

    assert result == "CUST-001"


def test_validate_customer_removes_extra_spaces():
    result = validate_customer("  CUST-001  ")

    assert result == "CUST-001"


def test_validate_customer_rejects_empty_customer():
    with pytest.raises(InvalidCustomerError):
        validate_customer("")


def test_validate_customer_rejects_non_string():
    with pytest.raises(InvalidCustomerError):
        validate_customer(123)


@patch("app.services.get_orders_by_customer")
def test_fetch_customer_orders(mock_repository):
    mock_repository.return_value = [
        {
            "name": "SO-001",
            "customer": "CUST-001",
            "grand_total": 1000,
        }
    ]

    result = fetch_customer_orders("CUST-001")

    assert len(result) == 1
    assert result[0]["name"] == "SO-001"

    mock_repository.assert_called_once_with(
        "CUST-001"
    )


@patch("app.services.get_orders_by_customer")
def test_fetch_customer_orders_handles_error(
    mock_repository,
):
    mock_repository.side_effect = Exception(
        "Repository failed"
    )

    with pytest.raises(OrderFetchError):
        fetch_customer_orders("CUST-001")