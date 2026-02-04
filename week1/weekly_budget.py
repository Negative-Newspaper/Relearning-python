daily_spenting = float(input("Enter Daily spending: "))
number_of_days = float(input("Enter number of days: "))

Total = daily_spenting * number_of_days
average = Total / number_of_days

print(f"Total spent:{Total: .2f}")
print(f"Average: {average: .2f}")
