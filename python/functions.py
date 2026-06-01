def display_invoice(username, amount):
    print("Generating invoice...")
    print("Please wait...")
    print("Invoice generated successfully!")
    print("-----------------------------")
    print("Invoice Details:")
    print("-----------------------------")
    print(f"Customer Name: {username}")
    print(f"Invoice for {username}: ${amount:.2f}")
    
    display_invoice("John Doe", 150.75)
