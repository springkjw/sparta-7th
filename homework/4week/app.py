# app.py
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order')
def order_get():
    orders = list(db.orders.find())
    return jsonify({
        "orders": orders
    })

@app.route('/order')
def order_post():
    return

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
