from invoice_app.models.invoice import Invoice
from invoice_app.services.invoice_service import(validate_data, calculate_total)
from invoice_app.repositories.invoice_repository import save_data

def get_invoice_input() -> Invoice:
    invoice_number = input("Enter invoice number:")
    customer_name = input("Enter customer name:")
    item_name = input("Enter item name:")
    quantity = int(input("Enter quantity:"))
    price = float(input("Enter price:"))
    invoice = Invoice(
        invoice_number=invoice_number,
        customer_name=customer_name,
        item_name=item_name,
        quantity=quantity,
        price=price
    )
    return invoice

def main():
    invoice = get_invoice_input()
    if not validate_data(invoice):
        print("Invalid invoice data. Please check the input values.")
        return
    total = calculate_total(invoice)
    save_data(invoice, total)
    print("Customer invoice report generated successfully.")
    print(f"Total Amount: {total}")

if __name__ == "__main__":
    main()