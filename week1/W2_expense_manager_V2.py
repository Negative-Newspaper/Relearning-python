def get_expenses():
    days = int(input("Enter days: "))
    
    expenses = []
    
    for day in range(days):
        expense = float(input("Enter Expense: "))
        category = input("Enter Category: ").strip().lower()
        summary_of_expense = {"Expense": expense, "Category" : category}
        expenses.append(summary_of_expense)
        
    return expenses

def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["Expense"]
    return total

def calcutate_average(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["Expense"]
    
    average = total/len(expense_list)
    return average

def all_Expenses(expense_list):
    print("All Expenses:")
    i = 1
    for expense in expense_list:
        print(f"{i}.", expense["Category"],"-", expense["Expense"])
        i += 1

def mixmax(expense_list):
    minExpense = expense_list[0]
    maxExpense = expense_list[0]
    
    for expense in expense_list:
        if expense["Expense"] > maxExpense["Expense"]:
            maxExpense = expense
        if expense["Expense"] < minExpense["Expense"]:
            minExpense = expense
    
    print(f"Highest:{maxExpense['Category']} - {maxExpense['Expense']}")
    print(f"Lowest:{minExpense['Category']} - {minExpense['Expense']}")

def show_category_totals(expense_list):
    
    total_by_category = {}
    
    for items in expense_list:
        
        category = items["Category"]
        amount = items["Expense"]
        
        if category not in total_by_category:
            total_by_category[category] = 0
        
        total_by_category[category] += amount
    print("Category totals: ")
    for key, value in total_by_category.items():
        print(f"{key}: {value}")
    
   
def show_summary(expense_list):
    
    all_Expenses(expense_list)
    print(f"Total: {calculate_total(expense_list)}")
    print(f"Average: {calcutate_average(expense_list)}")
    mixmax(expense_list)
    show_category_totals(expense_list)
    
def main():
    show_summary(get_expenses())

 
if __name__ == "__main__":
    main()
    
