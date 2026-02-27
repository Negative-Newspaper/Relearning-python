# A function to be get the user info and return a list of dictionary.
def get_expenses():
    days = int(input("Enter days: "))
    
    expenses = []
    
    for day in range(days):
        expense = float(input("Enter Expense: "))
        category = input("Enter Category: ").strip().lower()
        summary_of_expense = {"Expense": expense, "Category" : category}
        expenses.append(summary_of_expense)
        
    return expenses

# A function that get a list of dictionary from get_expenses function and return the total expense
def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["Expense"]
    return total

# A function that get a list of dictionary from get_expenses function and return the Average expense
def calcutate_average(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["Expense"]
    
    average = total/len(expense_list)
    return average

# A function that get a list of dictionary from a get_expenses fuction and Print all category and expense
def all_Expenses(expense_list):
    print("All Expenses:")
    i = 1
    for expense in expense_list:
        print(f"{i}.", expense["Category"],"-", expense["Expense"])
        i += 1

# A function that get a list of dictionay from a get_expense and print all the max and min expenses.
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


# a fuction that get a list of dictionary of get_expense fuction, add all the same category, then print it
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
    

# a fuction that act as a main hub for all the fuctions. 
def show_summary(expense_list):
    
    all_Expenses(expense_list)
    print(f"Total: {calculate_total(expense_list)}")
    print(f"Average: {calcutate_average(expense_list)}")
    mixmax(expense_list)
    show_category_totals(expense_list)
 
 # a fuction that gets the main hub    
def main():
    show_summary(get_expenses())

# an idiom that help not to us the fuction main() when using on a diffent file
if __name__ == "__main__":
    main()
    
