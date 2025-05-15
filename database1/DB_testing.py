import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('RNG_database.db')

# Query to select a random row
query = """
SELECT * FROM RNG_table
ORDER BY RANDOM()
LIMIT 1
"""

# Execute query and fetch results
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the result
print("Randomly selected game details:")
print(df)
