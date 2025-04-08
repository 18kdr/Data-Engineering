import requests
import json
import psycopg2
import pandas as pd

# Step 1 - Getting The data from the API

api_url = 'https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2023-2024'
response = requests.get(api_url)
data = response.json()

#Error Checking

if response.status_code == requests.codes.ok:
    print("")
    #print(json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)

# Step 2 - Extracting the data from the JSON response and converting it to a DataFrame

df = pd.DataFrame(data.get("table",[]))
#print(df.values)
print(df.columns)

# Step 3 - Storing the data 

# Storing the data in a CSV file
path = r'path_you_want_to_store_the_file_at'
df.to_csv(path, index=False)

# Storing the data in Postgres 

# Establishing the connection to the PostgreSQL database
# Note: Make sure to have PostgreSQL installed and running on your machine.
conn = psycopg2.connect(
    dbname= 'DB_NAME',
    user= 'USERNAME',
    password= 'PASSWORD', 
    host= 'HOSTNAME',
    port= 'PORT_ID' #(DEFAULT - 5432)
    )
# Creating a cursor object using the connection object
cur = conn.cursor()

# Checking if the connection is ready or not
if conn.status == psycopg2.extensions.STATUS_READY:
    print("Connection is ready.")
else:
    print("Connection not ready. Status code:", conn.status)
    
# Apporoach-2 Try-Catch block can be used too. 


# Create a table in league_standings_db database if it doesn't exist
create_script = '''
CREATE TABLE IF NOT EXISTS football_standings (
    idStanding INT,
    intRank INT,
    idTeam INT PRIMARY KEY,
    strTeam VARCHAR,
    strBadge VARCHAR,
    idLeague VARCHAR,
    strLeague VARCHAR,
    strSeason VARCHAR,
    strForm VARCHAR,
    strDescription VARCHAR,
    intPlayed INT,
    intWin INT,
    intLoss INT,
    intDraw INT,
    intGoalsFor INT,
    intGoalsAgainst INT,
    intGoalDifference INT,
    intPoints INT,
    dateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''
cur.execute(create_script)

insert_script = '''
    INSERT into football_standings(
    idStanding, intRank, idTeam, strTeam, strBadge, idLeague, strLeague, strSeason, strForm, strDescription,
    intPlayed, intWin, intLoss, intDraw, intGoalsFor, intGoalsAgainst, intGoalDifference, intPoints, dateUpdated
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

records = [tuple(rows) for rows in df.values]
cur.executemany(insert_script, records)

# Commit the changes to the database
# Note: If you don't commit, the changes will not be saved to the database.
conn.commit()

# To terminate the connection
cur.close()
conn.close()

# Data now set will try to generate insights from the data, the software used will be mostly POWER BI or Tableau.
# Key insight points from the data :- 
# Small description of the league standings data:
# 1 - Despite finishing 2nd in the league, Arsenal boost best defensive record in the league with just 
# 2 - Liverpool finished third however if they had won thier last 5 games they would have finished 1st. and eventual chamions 
# 3 - Sheffield United finished 20th with an astonishing 104 goals conceded in the league. Which is the most since PL started in 1992 ending the season with worst goal difference of -69.
# 4 - Qualifictaion of newcastle was halted even though they finished 7th in the league, because of the FA cup win by Manchester United and them finishing 8th in the league.
