from flask import Flask, request, jsonify, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Make sure index.html is in the correct folder

@app.route("/get_players", methods=["GET"])
def get_players():
    team = request.args.get("team")
    year = request.args.get("year")

    print(f"Received request: team={team}, year={year}")  # Debugging

    if not team or not year:
        return jsonify({"error": "Team and year are required"}), 400

    conn = sqlite3.connect('RNG_database.db')
    query = """
    SELECT firstName, lastName, position, points
    FROM RNG_table
    WHERE playerteamName = ? AND year = ?
    """
    df = pd.read_sql_query(query, conn, params=(team, year))
    conn.close()

    print(f"Query result: {df.to_dict(orient='records')}")  # Debugging
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
