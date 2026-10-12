# adds up all the expenses in the dict
# put a breakpoint on the total line to watch category and amount change
def calculate_monthly_budget(expenses):
    total = 0
    for category, amount in expenses.items():
        total += amount
    return total


monthly_expenses = {
    "Rent": 1200,
    "Groceries": 350,
    "Utilities": 150,
    "Entertainment": 100
}

total = calculate_monthly_budget(monthly_expenses)
print("Total Expense Calculated:", total)
