import csv
import datetime
import os

def save_transaction():
    today = datetime.datetime.today()
    now = today.strftime("%Y-%m-%d %H:%M:%S")
    file_exist = os.path.isfile("transaction.csv")
    
    with open("transaction.csv", mode="a", newline="") as file:
        write = csv.writer(file)
        
        if not file_exist:
            write.writerow(["Id", "Amount", "Category", "timeStamp"])
            
        write.writerow([1, 100, "food", now])
        
save_transaction()