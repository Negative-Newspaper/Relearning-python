import datetime

today1 = datetime.datetime.today()
now1 = today1.strftime("%Y-%m-%d %H:%M:%S")

expenses = []

#adding expenses
def add_expense():
    num_of_expense = int(input("enter how many expenses you will be adding: "))
    
    
    id = 1
    
    for day in range(num_of_expense):
        expense = float(input("Enter expenses"))
        category = input("Enter category: ")
        now = today.strftime("%Y-%m-%d %H:%M:%S")
        summary_of_expense = {"Id": id, "Expense": expense, "Category": category, "Time": now}
        id += 1
        expenses.append(summary_of_expense)
        
    return expenses


#searching expenses
def search_by_category(expense_list):
    
    category = input("Enter the category that you are searching: ")
    searched = category
    search_found = []
    for expense in expense_list:
        if expense["Category"] == searched:
            searched1 = {"Id": expense['Id'], "Expense": expense['Expense'], "Category":expense['Category'], "Time": expense['Time'] }
            search_found.append(searched1)
            
    print(search_found)
    for expense in search_found:
        if len(search_found) <= 0:
            print("Data did not found")
            break
        else:
            print(f"ID: {expense['Id']} | {expense['Category']} | {expense['Expense']} | {expense['Time']}")


# deleting expenses
def delete_transaction(expenses_list):
    print(expenses_list)
    Id_delete = int(input("Enter the ID that you want to delete: "))
    ID_del_found = []
    
    for expense in expenses_list:
        if expense["Id"] == Id_delete:
            ID_del_found.append(expense["Id"])
    
    if len(ID_del_found) > 0:
        print("Locatded ID")
    else:
        print("Data not found.")
        
    for expense in expenses_list:
        if expense["Id"] == Id_delete:
            expenses_list.remove(expense)
            print(f"Succesfuly remove Id number: {Id_delete}")
    
    
    print(expenses_list)   
        

# show expenses
def show_summary(expenses_list):
    print("All expenses: ")
    for expense in expenses_list:
        print(f"ID: {expense['Id']} | {expense['Category']} | {expense['Expense']} | {expense['Time']}")
    

def menu():
    print("1. Add transaction Please select 1")
    print("2. Show all please select 2")
    print("3. Search by Category please select 3")
    print("4. Delete please select 4")
    print("5. Exit please select 5 ")
    
    option = int(input("Please enter your choice: "))

    while option != 5:
        if option == 1:
            add_expense()
        elif option == 2:
            show_summary(expenses)
        elif option == 3:
            search_by_category(expenses)
        elif option == 4:
            delete_transaction(expenses)
            
        option = int(input("Please enter your choice: "))
    
    print("Program has exited.")   

menu()