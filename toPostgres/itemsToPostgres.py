import dlt
import os
import pandas as pd


# Set the directory where you want the script to run
desired_directory = r"C:\py_projects\Python\demo_git_cv"  # Change this to your desired path

# Change the current working directory
os.chdir(desired_directory)

filename = "items"
file_path = os.path.join(desired_directory,"sources","raw_files",filename+".csv")
print(file_path)

# Define the path to your CSV file
def read_csv_df(file_path,sep=";"):
    df = pd.read_csv(file_path,sep=sep)
    print(df.head(4)) 
    return df

df = read_csv_df(file_path)



# Initialize dlt pipeline
pipeline = dlt.pipeline(
    import_schema_path="schemas/import",
    export_schema_path="schemas/export",
    pipeline_name=filename, 
    destination="postgres",  #access dlt_toml
    dataset_name="raw"
)

# Load data into PostgreSQL
load_info = pipeline.run(df, table_name=filename, write_disposition="replace")

# Print the result
print(f"Data loaded: {load_info}")
