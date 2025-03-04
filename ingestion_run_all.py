from os import listdir
from os.path import isfile, join
import os

# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path
sub_directories = ["sources","toPostgres"]
directories = [os.path.join(desired_directory,f) for f in sub_directories]

for directory in directories:   
    print(directory)
    onlyfiles = [f for f in os.listdir(directory) if f.endswith(".py")]
    onylfilesPath = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".py")]
    print(onylfilesPath)
    for filePath in onylfilesPath:
        print('path: ',filePath)
        os.chdir(os.path.dirname(filePath))
        try:
            with open(filePath, "r") as f:
                code = f.read()
            exec(code)
            print("Script executed successfully.")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred during execution: {e}")