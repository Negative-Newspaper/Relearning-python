days = int(input("enter number of days: "))

expenses = []

for day in range(days):
    expense = float(input("Enter expnse today: "))
    expenses.append(expense)

for expense in expenses:
    if expense >= 500:
        print(expense)
    
