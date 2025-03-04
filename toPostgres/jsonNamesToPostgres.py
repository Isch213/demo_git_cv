import dlt
import os
import json

# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path

# Change the current working directory
os.chdir(desired_directory)


filename = "jsonNames"
file_path = os.path.join(desired_directory,"sources","raw_files",filename+".json")

name = "json_names"

# Step 1: Read the JSON file
with open(file_path, "r") as json_file:
    data = json.load(json_file)  # Load JSON as Python dict or list
    print(type(data))

    print(data)


pipeline = dlt.pipeline(
    pipeline_name = name,
    destination="postgres",
    dataset_name="raw"
)

load_info = pipeline.run(data, table_name=name ,write_disposition="append") 

# Print the result
print(f"Data loaded: {load_info}")