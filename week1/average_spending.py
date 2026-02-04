days = int(input("Enter number of days:"))

expenses = 0
for day in range(0, days):
    expense = float(input("Enter the expense for today: "))
    expenses += expense
    

average = expenses / days

print(f"Average per day:{average}")