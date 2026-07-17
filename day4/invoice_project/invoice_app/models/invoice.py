from dataclasses import dataclass
@dataclass
class Invoice:
    invoice_number: str
    customer_name: str
    item_name: str
    quantity: int
    price: float