days = int(input("Enter the number of days: "))

expenses = 0

for day in range(days):
    expense = float(input(f"Enter the your expese day{day+1}: "))
    expenses += expense
    
average = expenses / days

print(f"Average spent: {average}")

if average >= 500:
    print("Warning High spending!")
else:
    print("you are safe")
    
