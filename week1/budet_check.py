budget = float(input("Enter your daily budget: "))
spent = float(input("Enter amount spent"))

if spent > budget:
    print("You are over the budget")
elif spent == budget:
    print("You spent exactly your budget.")
else:
    print("good job you are with in the budget.")