import requests as req
import names
import json
import os

def API_names(API_length):    #List of random names
    lName=[]
    for i in range(API_length):
        rand_name=names.get_first_name()
        lName.append(rand_name)

    #Url and payload
    url = 'https://api.agify.io?'
    payload = {'name[]':lName,'country_id':'DE'}
    result = req.get(url,params=payload)

    #print Url with payload and output normalized json
    print('nr. of names: ',API_length,payload)
    return result.json()

# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path
# Change the current working directory
os.chdir(desired_directory)

# Get the directory where the script is located
file_path = os.path.join(desired_directory,"sources","raw_files", "jsonNames.json")

result = API_names(10)

with open (file_path,"w") as json_file:
    try:
        json.dump(result,json_file,indent=4)
        print(f"file saved in the directory {file_path}")
    except:
        print("Error: Response is not valid JSON")



