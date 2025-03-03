import dlt
import os
import pandas as pd


# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path

# Change the current working directory
os.chdir(desired_directory)

print(f"Current Working Directory: {os.getcwd()}")
print(f"Current script Directory: {os.path.dirname(os.path.abspath(__file__)) }")
sourcesdir =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = "de_holidays"
file_path = os.path.join(sourcesdir,"sources","raw_files",filename+".csv")
print(file_path)

# Define the path to your CSV file
def read_csv_df(file_path,sep=";"):
    df = pd.read_csv(file_path,sep=sep)
    print(df.head(4)) 
    return df

df = read_csv_df(file_path)



# Initialize dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name="de_holidays", 
    destination="postgres",  #access dlt_toml
    dataset_name="raw"  
)

# Load data into PostgreSQL
load_info = pipeline.run(df, table_name="de_holidays", write_disposition="replace")

# Print the result
print(f"Data loaded: {load_info}")
