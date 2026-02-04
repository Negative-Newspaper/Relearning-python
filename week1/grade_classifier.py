grade = float(input("Enter your grade: "))

if grade <= 100 and grade >= 90:
    print("A")
elif grade <= 89 and grade >= 80:
    print("B")
elif grade <= 79 and grade >= 75:
    print ("C")
else:
    print("F")