food_cost = float(input("Food cost: "))
transport_cost = float(input("Transprot cost:"))
other_cost = float(input("Other expenses: "))

total = food + transport + other

print(f"Food: {food_cost: .2f}")
print(f"Transport: {transport_cost: .2f}")
print(f"Other: {other_cost: .2f}")
print(f"Total spent today: {total: .2f}")