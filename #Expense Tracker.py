#Expense Tracker
expense_tracker = input("Welcome to your Expense Tracker! Say yes to add your expense: ")

expense = []

def insert_expense():
    description = input("Description: ")
    category = input("Category: ")
    amount = None
    while amount is None:
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Enter a valid amount.")
    expense.append((category, description, amount))
    print("Expense was added!")

def show_expenses():
    with open("Expensetracker.txt", "w") as f:
        for i, (category, description, amount) in enumerate(expense, 1):
            f.write(f"{i}. {category} - {description}: ${amount}\n")
    with open("Expensetracker.txt", "r") as f:
        print(f.read())

if expense_tracker.lower() == "yes":
    while True:
        print("Please choose an option:")
        print("1: Add an expense")
        print("2: Show expenses")
        print("3: Exit")
        user_input = input("Choice: ")
        if user_input == "1":
            insert_expense()
        elif user_input == "2":
            show_expenses()
        elif user_input == "3":
            print("Thanks for using my program!")
            break
        else:
            print("Invalid input, please enter 1, 2, or 3.")

