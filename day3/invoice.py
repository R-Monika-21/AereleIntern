from dataclasses import dataclass
@dataclass
class Invoice:
    invoice_number : str
    customer : str
    amount : float
    status : str
    paid : bool

class InvoiceController:
    def __init__(self, invoice : Invoice):
        self.invoice = invoice
    def validate(self):
        if not self.invoice.invoice_number:
            raise ValueError("Invoice number is empty!!")
        if self.invoice.customer == "":
            raise ValueError("Customer name is empty!!")
        valid_status = {"Pending", "Paid", "Cancelled", "Draft", "Submitted"}
        if self.invoice.status not in valid_status:
            raise ValueError("Invalid invoice status!!")
        if self.invoice.amount < 0:
            raise ValueError("Amount cannot be negative")
    def submit(self):
        self.validate()
        if self.invoice.status != "Draft":
            raise ValueError("Only draft invoices can be submitted!!")
        self.invoice.status = "Submitted"
    