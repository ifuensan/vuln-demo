import os, sqlite3
from flask import Flask, request
app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    return os.popen(f"ping -c 1 {host}").read()

@app.route("/user")
def user():
    uid = request.args.get("id", "")
    db = sqlite3.connect("app.db")
    return str(db.execute(f"SELECT name FROM users WHERE id ={uid}").fetchall())
