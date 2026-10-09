expenses = []

def add_expense():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")

        if category.strip() == "":                       # NEW: empty category check
            print("Category cannot be empty.")
            continue

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        if amount <= 0:                                  # NEW: reject zero/negative
            print("Amount must be greater than 0.")
            continue

        expense = {"date": date, "category": category, "amount": amount}
        expenses.append(expense)

        more = input("Do you want to add another expense? (yes/no): ")
        if more != 'yes':
            break
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")
summary = [expense['amount'] for expense in expenses]
print(f"Summary of Expenses: {summary}")
 