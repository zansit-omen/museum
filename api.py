import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from __init__ import set_up_database, seed_data

app = Flask(__name__)
database = ("anniversary.db")

def get_db():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods = ["GET"])
def see_photos():
    set_up_database()
    conn = get_db()
    cursor = conn.cursor()
    row = cursor.execute('''
                       SELECT url, description FROM photos;
                       ''').fetchall()
    if not row:
        return ("Error: No hay fotos")
    photos = [dict(photo) for photo in row]
    conn.close()
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    app.run (debug = True)