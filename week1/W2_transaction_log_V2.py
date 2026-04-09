import csv
import os
import datetime

today = datetime.datetime.today()
file_exist = os.path.isfile("transaction.csv")

def load_from_CSV_to_list(fileName):
    expense_list = []
    if not os.path.exists(fileName):
            return []
    else:
        with open(fileName, mode="r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try: 
                    row["ID"] = int(row["ID"])
                    row["Amount"] = float(row["Amount"])
                    expense_list.append(row)
                except ValueError:
                    print(f"Skipping invalid value in row:{row}")
                    continue
        return expense_list
        
expense_list = load_from_CSV_to_list("transaction.csv")

def add_expenses():
    expenses_to_add = int(input("How many expenses you will be adding? "))

    for expense in range(expenses_to_add):
        category = input("Enter the expense type: ")
        amount = float(input("Enter amount of expenses: "))
        time = today.strftime("%Y-%m-%d %H:%M:%S")
        expenses = {"ID": 1, "Time": time, "Category": category, "Amount": amount }
        expense_list.append(expenses)
    
    save_transaction(expense_list)

def save_transaction(expense_list):
    
    keyHeader = []
    
    if len(expense_list) > 0:
        for dic in expense_list[0]:
            keyHeader.append(dic)
    else:
        keyHeader = ["ID", "Time", "Category", "Amount"]
           
    with open("transaction.csv", mode="w", newline="") as file:
        write = csv.DictWriter(file, keyHeader)   
        write.writeheader()
        write.writerows(expense_list)

def delete_transaction(expense_list):
    Id_to_delete = int(input("Enter the ID that you want to delete: "))
    lst_to_delete = []
    
    for expense in expense_list:
        if expense["ID"] == Id_to_delete:
            lst_to_delete.append(expense["ID"])
            
    
    if len(lst_to_delete) > 0:
        print("Id found")
        for expense in reversed(expense_list):
            if expense["ID"] == Id_to_delete:
                expense_list.remove(expense) 
                print(f"Succesfuly remove Id number: {Id_to_delete}")
    else:
        print("Data not found.")
    
            
    save_transaction(expense_list)
    print(lst_to_delete)
    
def show_expenses():
    with open("transaction.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"ID: {row['ID']} | {row['Category']} | {row['Amount']} | {row['Time']}")
        
     
add_expenses()
show_expenses()