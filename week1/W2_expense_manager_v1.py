def get_expnses():
    days = int(input("Input days: "))
    
    expenses = []
    for day in range(days):
        expense = float(input("Enter days: "))
        expenses.append(expense)
        
    return expenses

def calculate_total(expenses_list):
    return sum(expenses_list)

def calculate_average(expenses_list):
    return sum(expenses_list)/ len(expenses_list)

def show_summary(expenses_list):
    print(expenses_list)
    print(calculate_total(expenses_list))
    print(calculate_average(expenses_list))
    print(max(expenses_list))
    print(min(expenses_list))
    
def filter_expenses(expenses):
    threshold = float(input("Enter spending goal for today"))
    
    if threshold >= expenses:
        print("over the buget")

def main():
    expenses = get_expnses()
    show_summary(expenses)
    
if __name__ == "__main__":
    main()