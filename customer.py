customers = []

def add_customer():

    print("\n--- ADD CUSTOMER---")
    customer_id = input("Enter the ID: ").strip()
    for customer in customers:
        if customer["id"] == customer_id:
            print("Customer already exists.")
            return

    name = input("Enter customer name: ").strip()
    address = input("Enter address: ").strip()
    phone_input = input("Enter phone: "). strip()
 
    phone = int(phone_input)

    if phone < 0:
        print("Phone cannot be negative.")
        return

    customer = {
        "id" : customer_id,
        "name" : name,
        "address" : address,
        "phone" : phone
    }
    customers.append(customer)
    print("Customer added successfully!.")

def view_customers():
    print("\n--- VIEW CUSTOMERS---")

    if not customers:
        print("No customers found.")
        return
    
    for customer in customers:
        print("---------------------")

        print("ID:", customer["id"])
        print("Name:", customer["name"])
        print("Address", customer["address"])
        print("Phone:", customer["phone"])

def search_customer():
    print("\n--- SEARCH CUSTOMER ---")

    customer_id = input("Enter customer ID: ").strip()

    for customer in customers:

        if customer["id"] == customer_id:
            print("customer found.")

            print("Name:", customer["name"])
            print("Department:", customer["address"])
            print("Phone:", customer["phone"])
            return
        
    print("Customer not found.")

def update_customer():
    print("\n---UPDATE CUSTOMER---")

    customer_id = input("Enter customer ID: ").strip()

    for customer in customers:
        if customer["id"] == customer_id:
            new_name = input("Enter new name (press enter to keep current)").strip()
            new_address = input("Enter new address (press enter to keep current)").strip()
            new_phone = input("Enter new phone (press enter to keep current)").strip()

            if new_name:
                customer["name"] = new_name
            if new_address:
                customer["address"] = new_address
            if new_phone:
                customer["phone"] = new_phone
            print("Customer updated successfully!")
            return

def delete_customer():
    print("\n--- DELETE CUSTOMER---")

    customer_id = input("Enter customer ID: ").strip()

    for customer in customers:
        if customer["id"] == customer_id:
            customers.remove(customer)
            print("Customer deleted successfully!")
            return
        print("Customer not found.")

def main():
    while True:
        print("\n========================")
        print("     CUSTOMER MANAGEMENT     ")
        print("\n========================")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            update_customer()
        elif choice == "5":
            delete_customer()
        elif choice == "6":
            print("Thank you for using customer management.")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()