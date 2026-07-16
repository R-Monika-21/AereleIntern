from dataclasses import dataclass
@dataclass
class Invoice:
    invoice_number : str
    customer : str
    amount : float
    status : str
    paid : bool
    