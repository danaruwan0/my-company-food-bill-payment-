from datetime import datetime

# Prices
BREAKFAST_PRICE = 150
LUNCH_DINNER_PRICE = 250

# Users and Transactions Data
users = {
    "ui001": "Manager Ratnasinha",
    "ui002": "Assistant Manager Chameera",
    "ui003": "Cash Officer Nuwan Rathnayaka",
    "ui004": "Bhanuka",
    "ui005": "Lkshan",
    "ui006": "Isuru",
    "ui007": "Damith",
    "ui008": "Diwantha",
    "ui009": "Thisoka",
    "ui010": "Pathum",
    "ui011": "Senuri",
    # Add all users here...
}
transactions = []

def add_transaction(user_id, meal_type, quantity, amount_paid, date_time):
    transaction = {
        "user_id": user_id,
        "meal_type": meal_type,
        "quantity": quantity,
        "amount_paid": amount_paid,
        "date_time": date_time,
        "change_due": calculate_change(meal_type, quantity, amount_paid)
    }
    transactions.append(transaction)

def calculate_cost(meal_type, quantity):
    if meal_type in ["breakfast"]:
        return BREAKFAST_PRICE * quantity
    elif meal_type in ["lunch", "dinner"]:
        return LUNCH_DINNER_PRICE * quantity
    else:
        return 0

def calculate_change(meal_type, quantity, amount_paid):
    total_cost = calculate_cost(meal_type, quantity)
    return amount_paid - total_cost

def display_transaction(transaction):
    print("User ID:", transaction["user_id"])
    print("Meal Type:", transaction["meal_type"])
    print("Quantity:", transaction["quantity"])
    print("Amount Paid:", transaction["amount_paid"])
    print("Date and Time:", transaction["date_time"])
    print("Change Due:", transaction["change_due"])

def show_details(user_id):
    for transaction in transactions:
        if transaction["user_id"] == user_id:
            display_transaction(transaction)

def main():
    while True:
        user_id = input("Enter User ID: ")
        if user_id not in users:
            print("User not found. Please try again.")
            continue
        
        meal_type = input("Enter meal type (breakfast/lunch/dinner): ").lower()
        quantity = int(input("Enter quantity: "))
        amount_paid = float(input("Enter amount paid: "))
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_transaction(user_id, meal_type, quantity, amount_paid, date_time)

        action = input("Enter 'continue' to add more, 'show' to view details, or 'exit': ").lower()
        if action == "show":
            show_details(user_id)
        elif action == "exit":
            break

if __name__ == "__main__":
    main()
