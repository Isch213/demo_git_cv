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


# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path

# Change the current working directory
os.chdir(desired_directory)

# save loc
file_path = os.path.join(desired_directory,"sources","raw_files", "lisDates.csv")  

try:
    print('starting to try to save csv')
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(["dates"])
        for item in lisDates:
                writer.writerow([item])  # Each item in a new row
        print(f"Success - CSV file saved at: {file_path}")
except IOError as e:  # Handles file-related errors (e.g., permission issues, disk full)
    print(f"Error saving file: {e}")
except Exception as e:  # Catches any other unexpected errors
    print(f"An unexpected error occurred: {e}")