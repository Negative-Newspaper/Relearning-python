numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
    
print("numbers:", numbers)
print("Total", sum(numbers))
