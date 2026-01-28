total = 0

days = int(input("How many days?"))

for day in range(1, days + 1):
    expense = float(input(f"Expenses for day{day}:"))
    total += expense
    

print(f"Total Expenses: {total: .2f}")