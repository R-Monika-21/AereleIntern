def get_invoice_data():
    invoice_number = input("Enter the invoice number:")
    customer_name = input("Enter the customer name:")
    item_name = input("Enter the item name:")
    quantity = int(input("Enter the quantity:"))
    price = float(input("Enter the price:"))
    invoice = {
        "invoice_number": invoice_number,
        "customer_name": customer_name,
        "item_name": item_name,
        "quantity": quantity,
        "price": price
        }
    return invoice

def validate_data(invoice):
    if invoice["quantity"] <= 0:
        return False
    if invoice["price"] <= 0:
        return False
    if invoice["customer_name"] == "":
        return False
    return True
def calculate_total(invoice):
    return invoice["quantity"] * invoice["price"]
def save_data(invoice, total):
    with open(f"{invoice["customer_name"]}_invoice.txt", "a") as file:
        file.write(f"Invoice Number: {invoice['invoice_number']}\n")
        file.write(f"Customer Name: {invoice['customer_name']}\n")
        file.write(f"Item: {invoice['item_name']}\n")
        file.write(f"Quantity: {invoice['quantity']}\n")
        file.write(f"Price: {invoice['price']}\n")
        file.write(f"Total: {total}\n")
        file.write("-" * 30 + "\n")
def main():
    invoice = get_invoice_data()
    if not validate_data(invoice):
        print("Invoice data in invalid")
        return
    total  = calculate_total(invoice)
    save_data(invoice, total)
    print("Invoice data saved successfully")
    print(f"Total amount: {total}")
if __name__ == "__main__":
    main()