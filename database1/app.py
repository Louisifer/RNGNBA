from flask import Flask, request, jsonify, render_template
import sqlite3
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests when using different domains

def query_players(team, year):
    """Helper function to query players data by team and year from the database."""
    query = """
    SELECT firstName, lastName, ROUND(AVG(RNGscore), 2) AS avgRNGscore
    FROM RNG_table
    WHERE playerteamName = ? AND year = ?
    GROUP BY firstName, lastName
    """
    with sqlite3.connect('RNG_database.db') as conn:
        return pd.read_sql_query(query, conn, params=(team, year))

@app.route("/")
def home():
    # Ensure index.html exists in the "templates" folder.
    return render_template("index.html")

@app.route("/get_players", methods=["GET"])
def get_players():
    team = request.args.get("team")
    year = request.args.get("year")
    
    if not team or not year:
        return jsonify({"error": "Team and year are required"}), 400

    try:
        year = int(year)
    except ValueError:
        return jsonify({"error": "Year must be an integer"}), 400

    df = query_players(team, year)
    
    if df.empty:
        return jsonify({"message": "No players found for the selected team and year"}), 404

    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)




