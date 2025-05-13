import pandas as pd
import sqlite3

dtype1 = {10: str, 11: str}
df = pd.read_csv("RNGmasterStats.csv", dtype=dtype1)

conn = sqlite3.connect('RNG_database.db')

# Load DataFrame into SQL table
table_name = 'RNG_table'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()



