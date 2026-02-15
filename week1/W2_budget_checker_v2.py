days = int(input("Enter days: "))

def get_expense(days):
    expenses = []
    
    for day in range(days):
        expense = float(input("Enter expense for today: "))
        expenses.append(expense)
        
    return expenses
        
def expenses_total(expense):
    return sum(expense)

def expense_average(expense):
    return sum(expense) / len(expense)

def print_expnese(days):
    my_expense_list = get_expense(days)
    print(expenses_total(my_expense_list))
    print(expense_average(my_expense_list))

print_expnese(days)

    