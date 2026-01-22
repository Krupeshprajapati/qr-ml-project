from flask import Flask, request, render_template, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            email TEXT,
            device TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "<h2>QR ML Website Running</h2><p>Go to /scan</p>"

@app.route("/scan")
def scan():
    return render_template("scan.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    device = request.headers.get("User-Agent")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES (?,?,?,?)",
        (name, email, device, time)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})

@app.route("/data")
def show_data():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template("data.html", rows=rows)

if __name__ == "__main__":
    init_db()
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)

# import os

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     app.run(host="0.0.0.0", port=port)


