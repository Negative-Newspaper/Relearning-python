days = int(input("Enter number of days: "))

expenses = []

for day in range(days):
    expense = float(input("Enter expense for today: "))
    expenses.append(expense)

def calculate_total(expenses):
    return sum(expenses)

def calulate_average(expenses):
    return sum(expenses) / len(expenses)

print(calculate_total(expenses))
print(calulate_average(expenses))