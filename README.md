Paytm Backend API (Flask)

This project is a simple Paytm-like backend system built using Flask and SQLite.
It allows users to create accounts, check balances, send money, and view transaction history.

Technologies Used

Python

Flask

SQLite

Postman (API Testing)

Features

Create User

Check Balance

Send Money

Transaction History

API Endpoints
1. Create User

POST /create-user

Example JSON:
{
"name": "Kusu",
"balance": 1000
}

2. Check Balance

GET /balance/

Example:
GET /balance/Kusuma

3. Send Money

POST /send-money

Example JSON:
{
"sender": "Kusu",
"receiver": honey",
"amount": 200
}

4. Transaction History

GET /transactions

How to Run the Project

Install dependencies

pip install -r requirements.txt

Run Flask server

python app.py

Server runs at:
http://127.0.0.1:5000

Testing

All APIs were tested using Postman.
