# Ask user for number of days
# loop through each day
# Ask for expenses
# Add to total
# Calculate average
# If average > budget, warn user
# print summary

days = int(input("Enter the number of days: "))
budget = float(input("Enter you daily budget: "))

expenses = 0
over_the_budget = 0


for day in range(days):
    expense = float(input(f"Day{day + 1} your expenses: "))
    if expense >= budget:
        over_the_budget += 1
    expenses += expense
    
average = expenses / days

print(f"Total spent: {expenses}")
print(f"Average per day: {average}")
print(f"Days over the budget: {over_the_budget}")

if average > budget:
    print("Warning you are over the buget")
else:
    print("You stayed within your budget")
    