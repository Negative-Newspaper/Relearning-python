days = int(input("Input the number of days: "))

expenses = []

for day in range(days):
    expense = float(input("Enter the expense today: "))
    expenses.append(expense)


average = sum(expenses)/days
   
print("List of Expenses: ", expenses)
print("Total", sum(expenses))
print("Average", average)

