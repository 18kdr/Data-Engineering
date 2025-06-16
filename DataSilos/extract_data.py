import pandas as pd
import psycopg2


# extract SQL data
def extract_sql(dbname, user, password, host='localhost'):
    """Extract data from a SQL database."""
    conn1 = psycopg2.connect(
    dbname= dbname,
    user= user,
    password= password,
    host=host,
    )
    cur = conn1.cursor()
    query = "SELECT * FROM mock_data"
    df_sql = pd.read_sql(query,con=conn1)
    return df_sql

# Extracting data from a CSV file 
def extract_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Extracting Data from a JSON file 
def extract_json(file_path):
    df = pd.read_json(file_path)
    return df

def merge_df(dataframes):
    """Concatenate multiple DataFrames into one."""
    df_master = pd.concat(dataframes, ignore_index = True)
    df_master['master_id'] = df_master.index + 1
    return df_master

