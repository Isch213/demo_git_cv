from datetime import date, timedelta
import os
import csv


sdate = date(2025,1,1)
edate = date(2099,12,31)

lisDates = []
dates = sdate

for n in range((edate-sdate).days+1):
    lisDates.append(sdate+timedelta(days=n))
    #print(sdate+timedelta(days=n))
print(lisDates[:3])



# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(script_dir, "lisDates.csv")  # Save in the same directory as script


with open(file_path, "w", newline="") as file:
    writer = csv.writer(file,delimiter=";")
    writer.writerow(["dates"])
    for item in lisDates:
            writer.writerow([item])  # Each item in a new row

print(f"CSV file saved at: {file_path}")