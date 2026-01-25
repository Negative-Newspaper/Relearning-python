food = float(input("Food cost: "))
transport = float(input("Transprot cost:"))
other = float(input("Other expenses: "))

total = food + transport + other

print(f"Food: {food: .2f}")
print(f"Transport: {transport: .2f}")
print(f"Other: {other: .2f}")
print(f"Total spent today: {total: .2f}")