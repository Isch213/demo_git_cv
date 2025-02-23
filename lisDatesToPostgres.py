import dlt
import os
import pandas as pd

print(f"Current Working Directory: {os.getcwd()}")
print(f"Current script Directory: {os.path.dirname(os.path.abspath(__file__)) }")

# Define the path to your CSV file
def read_csv_df(filename,sep=";"):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    print(path)
    df = pd.read_csv(path,sep=sep)
    print(df.head(4)) 
    return df

df = read_csv_df("lisDates.csv")



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
