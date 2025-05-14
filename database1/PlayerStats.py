import pandas as pd
import sqlite3
import random

dtype1 = {10: str, 11: str}
df = pd.read_csv("RNGmasterStats.csv", dtype=dtype1)

conn = sqlite3.connect('RNG_database.db')

# Load DataFrame into SQL table
table_name = 'RNG_table'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Connect to the database
conn = sqlite3.connect('RNG_database.db')
cursor = conn.cursor()

# Generate a random game number
game_num = random.randint(1, 82)

# Query to fetch the game details for LeBron James with the selected game number
query = f"""
SELECT * FROM RNG_table
WHERE firstName = 'LeBron' AND lastName = 'James' AND year = '2017' AND gameNum = {game_num}
"""

# Execute the query and load results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the result
if not df.empty:
    print(f"Game {game_num} details for LeBron James:")
    print(df)
else:
    print(f"No game found for LeBron James with gameNum {game_num}.")

# Close the connection
conn.close()



