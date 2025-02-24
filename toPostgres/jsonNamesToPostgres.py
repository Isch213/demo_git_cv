import dlt
import os
import json

print(f"Current Working Directory: {os.getcwd()}")
print(f"Current script Directory: {os.path.dirname(os.path.abspath(__file__)) }")
filename = "jsonNames"
file_path = os.path.join(os.getcwd(),"sources","raw_files",filename+".json")

name = "json_names"

# Step 1: Read the JSON file
with open(file_path, "r") as json_file:
    data = json.load(json_file)  # Load JSON as Python dict or list
    print(type(data))

    print(data)


pipeline = dlt.pipeline(
    pipeline_name = name,
    destination="postgres",
    dataset_name=name
)

load_info = pipeline.run(data, table_name=name ,write_disposition="append") 

# Print the result
print(f"Data loaded: {load_info}")