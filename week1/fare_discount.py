age = int(input("Enter age: "))
student = input("Are you a student?: (yes/no)").strip().lower()

if student in ["yes"]:
    student = True
else:
    student = False

if age >= 60:
    print("Discount applied: 50%")
elif student == True:
    print("Discount appliend: 20%")
else:
    print("no discount")
