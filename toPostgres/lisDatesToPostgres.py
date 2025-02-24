import dlt
import os
import pandas as pd

print(f"Current Working Directory: {os.getcwd()}")
print(f"Current script Directory: {os.path.dirname(os.path.abspath(__file__)) }")
filename = "lisDates"
file_path = os.path.join(os.getcwd(),"sources","raw_files",filename+".csv")
print(file_path)

# Define the path to your CSV file
def read_csv_df(file_path,sep=";"):
    df = pd.read_csv(file_path,sep=sep)
    print(df.head(4)) 
    return df

df = read_csv_df(file_path)



# Initialize dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name="lisDates", 
    destination="postgres",  #access dlt_toml
    dataset_name="raw"  
)

# Load data into PostgreSQL
load_info = pipeline.run(df, table_name="lisDates", write_disposition="replace")

# Print the result
print(f"Data loaded: {load_info}")
