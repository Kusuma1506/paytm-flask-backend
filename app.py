from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------- CREATE TABLES ----------
def create_tables():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        balance INTEGER
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT,
        amount INTEGER
    )
    """)

    conn.commit()


# ---------- HOME ----------
@app.route("/")
def home():
    return "Paytm Backend Running"


# ---------- CREATE USER ----------
@app.route("/create-user", methods=["POST"])
def create_user():

    data = request.json
    name = data["name"]
    balance = data["balance"]

    conn = get_db()

    conn.execute(
        "INSERT INTO users (name,balance) VALUES (?,?)",
        (name, balance)
    )

    conn.commit()

    return jsonify({"message": "User created"})


# ---------- CHECK BALANCE ----------
@app.route("/balance/<name>")
def check_balance(name):

    conn = get_db()

    user = conn.execute(
        "SELECT balance FROM users WHERE name=?",
        (name,)
    ).fetchone()

    if user is None:
        return jsonify({"error": "User not found"})

    return jsonify({"balance": user["balance"]})


# ---------- SEND MONEY ----------
@app.route("/send-money", methods=["POST"])
def send_money():

    data = request.json

    sender = data["sender"]
    receiver = data["receiver"]
    amount = data["amount"]

    conn = get_db()

    # Deduct sender balance
    conn.execute(
        "UPDATE users SET balance = balance - ? WHERE name=?",
        (amount, sender)
    )

    # Add receiver balance
    conn.execute(
        "UPDATE users SET balance = balance + ? WHERE name=?",
        (amount, receiver)
    )

    # Record transaction
    conn.execute(
        "INSERT INTO transactions (sender,receiver,amount) VALUES (?,?,?)",
        (sender, receiver, amount)
    )

    conn.commit()

    return jsonify({"message": "Money Sent"})


# ---------- TRANSACTION HISTORY ----------
@app.route("/transactions")
def transactions():

    conn = get_db()

    tx = conn.execute(
        "SELECT * FROM transactions"
    ).fetchall()

    result = []

    for t in tx:
        result.append(dict(t))

    return jsonify(result)


# ---------- RUN SERVER ----------
if __name__ == "__main__":
    create_tables()
    app.run(debug=True)