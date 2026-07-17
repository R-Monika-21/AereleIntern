from invoice_app.models.invoice import Invoice
def save_data(invoice: Invoice, total: float) -> None:
    with open(f"{invoice.customer_name}_invoice_report.txt", "w") as file:
        file.write(f"Invoice Number: {invoice.invoice_number}\n")
        file.write(f"Customer Name: {invoice.customer_name}\n")
        file.write(f"Item: {invoice.item_name}\n")
        file.write(f"Quantity: {invoice.quantity}\n")
        file.write(f"Price: {invoice.price}\n")
        file.write(f"Total: {total}\n")
        file.write("-" * 30 + "\n")
