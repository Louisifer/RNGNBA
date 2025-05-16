from flask import Flask, request, jsonify, render_template
import sqlite3
import pandas as pd
from flask_cors import CORS  # Enable CORS if needed

app = Flask(__name__)
CORS(app)  # Allow frontend requests if running on different domains

@app.route("/")
def home():
    return render_template("index.html")  # Make sure index.html is in the "templates" folder

@app.route("/get_players", methods=["GET"])
def get_players():
    team = request.args.get("team")
    year = request.args.get("year")
    print(f"Received request: team={team}, year={year}")
    
    if not team or not year:
        return jsonify({"error": "Team and year are required"}), 400

    query = """
    SELECT firstName, lastName, ROUND(AVG(RNGscore), 2) AS avgRNGscore
    FROM RNG_table
    WHERE playerteamName = ? AND year = ?
    GROUP BY firstName, lastName
    """
    # Use a context manager to ensure safe DB operations
    with sqlite3.connect('RNG_database.db') as conn:
        df = pd.read_sql_query(query, conn, params=(team, year))
    
    if df.empty:
        return jsonify({"message": "No players found for the selected team and year"}), 404

    print(df.to_dict(orient="records"))
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

