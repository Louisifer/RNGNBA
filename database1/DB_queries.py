import sqlite3
import random
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_game', methods=['GET'])
def get_game():
    game_num = random.randint(1, 82)
    conn = sqlite3.connect('RNG_database.db')
    query = f"""
    SELECT * FROM RNG_table
    WHERE playerteamName = 'Cavaliers' AND year = '2017' AND gameNum = {game_num}
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
