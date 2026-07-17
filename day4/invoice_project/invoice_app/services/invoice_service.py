from invoice_app.models.invoice import Invoice
from invoice_app.utils.config import TAX_RATE
def validate_data(invoice: Invoice) -> bool:
    if invoice.invoice_number == "":
        return False
    if invoice.customer_name == "":
        return False
    if invoice.item_name == "":
        return False
    if invoice.quantity <= 0:
        return False
    if invoice.price < 0:
        return False
    return True
def calculate_subtotal(invoice: Invoice) -> float:
    return invoice.quantity * invoice.price
def calculate_tax(invoice: Invoice) -> float:
    subtotal = calculate_subtotal(invoice)
    return subtotal * TAX_RATE
def calculate_total(invoice: Invoice) -> float:
    subtotal = calculate_subtotal(invoice)
    tax = calculate_tax(invoice)
    return subtotal + tax
