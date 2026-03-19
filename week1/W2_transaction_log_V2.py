import csv
import os
import datetime

today = datetime.datetime.today()
file_exist = os.path.isfile("transaction.csv")
expense_list = []

def add_expenses():
    expenses_to_add = int(input("How many expenses you will be adding? "))

    for expense in range(expenses_to_add):
        category = input("Enter the expense type: ")
        amount = float(input("Enter amount of expenses: "))
        time = today.strftime("%Y-%m-%d %H:%M:%S")
        expenses = {"ID": 1, "Time": time, "Category": category, "Amount": amount }
        expense_list.append(expenses)

def save_transaction(expense_list):
    keys = expense_list[0]
    
    with open("transaction.csv", mode="a", newline="") as file:
        write = csv.DictWriter(file, keys)
        
        if not file_exist:
            write.writeheader()
        
        write.writerows(expense_list)
    
add_expenses()

save_transaction(expense_list)

print(expense_list)