from datetime import date
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

monthly_budget = None


def add_expense(expenses: list[dict]) -> None:
    print("\nAdd a new expense")

    amount_str = input("Amount (e.g., 120.50): ").strip()
    category = input("Category (e.g., Food/Travel/Rent): ").strip()
    description = input("Description (e.g., Uber Auto): ").strip()

    if not amount_str:
        print(Fore.RED + "Amount cannot be empty.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        print(Fore.RED + "Amount must be a number.")
        return

    if amount <= 0:
        print(Fore.RED + "Amount must be greater than 0.")
        return

    if not category:
        print(Fore.RED + "Category cannot be empty.")
        return

    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print(Fore.GREEN + "Expense added successfully!")


def list_expenses(expenses: list[dict]) -> None:
    print("\nAll expenses")

    if not expenses:
        print("No expenses found yet.")
        return

    rows = []
    for i, e in enumerate(expenses, start=1):
        rows.append([i, e["date"], e["amount"], e["category"], e["description"]])

    print(tabulate(rows, headers=["No", "Date", "Amount", "Category", "Description"], tablefmt="grid"))


def show_total(expenses: list[dict]) -> None:
    total = sum(float(e["amount"]) for e in expenses)

    print(f"\nTotal spending: ₹{total:.2f}")

    global monthly_budget
    if monthly_budget and total > monthly_budget:
        print(Fore.RED + "WARNING: Budget exceeded!")


def show_category_summary(expenses: list[dict]) -> None:
    print("\nCategory summary")

    if not expenses:
        print("No expenses found yet.")
        return

    summary = {}
    for e in expenses:
        cat = e["category"]
        amt = float(e["amount"])
        summary[cat] = summary.get(cat, 0.0) + amt

    rows = []
    for cat, amt in summary.items():
        rows.append([cat, f"₹{amt:.2f}"])

    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))


def delete_expense(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses to delete.")
        return

    list_expenses(expenses)

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(Fore.GREEN + f"Deleted expense: {removed['description']}")
        else:
            print(Fore.RED + "Invalid number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")


def edit_expense(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses to edit.")
        return

    list_expenses(expenses)

    try:
        index = int(input("Enter expense number to edit: ")) - 1
        if 0 <= index < len(expenses):
            expense = expenses[index]

            new_amount = input(f"New amount ({expense['amount']}): ").strip()
            new_category = input(f"New category ({expense['category']}): ").strip()
            new_description = input(f"New description ({expense['description']}): ").strip()

            if new_amount:
                expense["amount"] = float(new_amount)
            if new_category:
                expense["category"] = new_category
            if new_description:
                expense["description"] = new_description

            print(Fore.GREEN + "Expense updated.")
        else:
            print(Fore.RED + "Invalid number.")
    except ValueError:
        print(Fore.RED + "Invalid input.")


def monthly_report(expenses: list[dict]) -> None:
    month = input("Enter month (YYYY-MM): ").strip()

    filtered = [e for e in expenses if e["date"].startswith(month)]

    if not filtered:
        print("No expenses for this month.")
        return

    list_expenses(filtered)

    total = sum(float(e["amount"]) for e in filtered)
    print(f"\nTotal for {month}: ₹{total:.2f}")


def set_budget(expenses: list[dict]) -> None:
    global monthly_budget

    try:
        monthly_budget = float(input("Set monthly budget: "))
        print(Fore.GREEN + f"Budget set to ₹{monthly_budget:.2f}")
    except ValueError:
        print(Fore.RED + "Invalid number.")