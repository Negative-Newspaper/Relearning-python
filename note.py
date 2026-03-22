import csv
import datetime
import os

def save_transaction():
    today = datetime.datetime.today()
    now = today.strftime("%Y-%m-%d %H:%M:%S")
    
    file_exist = os.path.isfile("transaction.csv")
    
    inputs = int(input("Enter number of input: "))
    
    for number_input in range(inputs):
        
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
    
        with open("transaction.csv", mode="a", newline="") as file:
            write = csv.writer(file)
            
            if not file_exist:
                write.writerow(["Id", "Amount", "Category", "timeStamp"])
                
            write.writerow([1, amount, category, now])
        
def load_from_scv():
    
    with open("transaction.csv", mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader: 
            print(row)

load_from_scv()



#crate a expense and save it to CSV
"""
steps:

Ask AH on how many days he/she will be inputing(done)

Ask the expense and category he/she will be inputing. (done)

The ID and date must be automatic.

save it on s list of dictionary (done)

auto seve it on a CSV

add auto load (done)

add auto save

"""