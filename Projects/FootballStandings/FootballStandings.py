import requests
import json
import psycopg2
import pandas as pd

# Getting The data from the API

api_url = 'https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2023-2024'
response = requests.get(api_url)
data = response.json()

#Error Checking 

if response.status_code == requests.codes.ok:
    print("")
    #print(json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)

# Extracting the data from the JSON response and converting it to a DataFrame

df = pd.DataFrame(data.get("table",[]))
#print(df.values)
print(df.columns)

# Storing the data in a CSV file
df.to_csv('football_standings.csv', index=False)

# Storing the data in Postgres Database
