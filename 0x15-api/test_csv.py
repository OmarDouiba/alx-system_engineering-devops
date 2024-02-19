#!/usr/bin/python3
import csv




with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["SNo", "Name", "Subject"])
    writer.writerow([1, "Ash Ketchum", "English"])
    writer.writerow([2, "Gary Oak", "Mathematics"])
    writer.writerow([3, "Brock Lesner", "Physics"])


with open("students.csv", 'r') as file:
    cvsreader = csv.reader(file)
    for row in cvsreader:
        print(row)

#we can write all rows in one time
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["SNo", "Name", "Subject"])
    writer.writerow([1, "Ash Ketchum", "English"])
    writer.writerow([2, "Gary Oak", "Mathematics"])
    writer.writerow([5, "Brock Lesner", "Physics"])


import pandas as pd
data = pd.read_csv("students.csv")
print(data)


