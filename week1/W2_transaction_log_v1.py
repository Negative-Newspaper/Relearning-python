import datetime


#adding expenses
def get_expense():
    days = int(input("enter days"))
    today = datetime.datetime.today()
    expenses = []
    
    id = 1
    
    for day in range(days):
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
            searched = {"Id": expense['Id'], "Expense": expense['Expense'], "Category":expense['Category'], "Time": expense['Time'] }
            search_found.append(searched)
            
       
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
    
# running a single function(checking if is doing what intended it does to do.)   
delete_transaction(get_expense())

        
        