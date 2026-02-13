days = int(input("Enter number of days: "))

def get_expense(days):
    expenses = []
       
    for day in range(days):
        expense = float(input("Enter expense for today: "))
        expenses.append(expense)
    
    return expenses

def calculate_total(expenses):
    return sum(expenses)
        
def calculate_average(expenses):
    return sum(expenses) / len(expenses)

def print_info(days):
    myExpenseList = get_expense(days)
    print(calculate_average(myExpenseList))
    print(calculate_total(myExpenseList))

print_info(days)
