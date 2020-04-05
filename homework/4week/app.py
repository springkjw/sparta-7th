# app.py
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order', methods=["GET"])
def order_get():
    orders = list(db.orders.find())
    return jsonify({
        "orders": orders
    })

@app.route('/order', methods=["POST"])
def order_post():
    name = request.form["name"]
    amount = request.form["amount"]
    address = request.form["address"]
    phone = request.form["phone"]

    print(name, amount, address, phone)

    return jsonify({"success": "OK"})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
