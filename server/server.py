from flask import Flask, request
from flask_restful import Api
import sqlite3
import os
from datetime import datetime, timedelta

today = datetime.now()
next_monday = today + timedelta(days=-today.weekday(), weeks=1)
end = next_monday + timedelta(days=6)
today = today.strftime("%Y-%b-%d %H:%M")
next_monday = next_monday.strftime("%Y-%b-%d")
end = end.strftime("%Y-%b-%d")

app = Flask(__name__)
api = Api(app)

dir = os.path.dirname(__file__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(dir, os.pardir,'client', 'data', 'sqlite3.db'))
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return "Server is up & running", 200

@app.route('/neos')
def neos():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute(
        "SELECT * FROM neos WHERE next_approach>='{}' ORDER BY next_approach".format(
            today
        )
    )
    rows = cursor.fetchall()
    conn.close()

    neos = []
    for row in rows:
        neo = {}
        neo["id"] = row[0]
        neo["name"] = row[1]
        neo["jpl_url"] = row[2]
        neo["is_hazardous"] = row[3]
        neo["next_approach"] = row[4]
        neos.append(neo)

    return {"neos approaching in the coming  days": neos}

@app.route('/neo/week')
def count():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute(
        "SELECT * FROM neos WHERE next_approach BETWEEN '{}' AND '{}' ORDER BY next_approach".format(
            next_monday, end
        )
    )
    rows = cursor.fetchall()
    conn.close()

    return {"number of neos approaching next week": len(rows)}

@app.route('/neo/next')
def next():
    is_hazardous = request.args.get("hazardous")

    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute(
        "SELECT * FROM neos WHERE is_hazardous={} AND next_approach>='{}' ORDER BY next_approach".format(
            is_hazardous, today
        )
    )
    rows = cursor.fetchall()
    conn.close()

    neo = {}
    neo["id"] = rows[0][0]
    neo["name"] = rows[0][1]
    neo["jpl_url"] = rows[0][2]
    neo["is_hazardous"] = rows[0][3]
    neo["next_approach"] = rows[0][4]

    return {"next hazardous neo": neo}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)