import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import mysql.connector

from datetime import datetime
import json

db = mysql.connector.connect(
    host="cme-g1t4-db.cnbzfopclntw.ap-southeast-1.rds.amazonaws.com",
    port="3306",
    user="admin",
    passwd="9uj\{hFi1\}21C",
    db="customer"
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') #unsure
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

# Customer Class/Model (customerEmail, phoneNum, bankNum, homeAddress)
class Customer(db.Model):
    __tablename__ = 'customer'

    customerEmail = db.Column(db.String(64), primary_key=True)
    phoneNum = db.Column(db.String(64), nullable=False)
    bankNum = db.Column(db.String(64), nullable=False)
    homeAddress = db.Column(db.String(64), nullable=False)

    def __init__(self, customerEmail, phoneNum, bankNum, homeAddress):
        self.customerEmail = customerEmail
        self.phoneNum = phoneNum
        self.bankNum = bankNum
        self.homeAddress = homeAddress

    def json(self):
        return {"customerEmail": self.customerEmail, 
                "phoneNum": self.phoneNum, 
                "bankNum": self.bankNum, 
                "homeAddress": self.homeAddress}






#routes
@app.route("/customer")
def get_all():
    customerlist = Customer.query.all()
    if len(customerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "customers": [customer.json() for customer in customerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404

@app.route("/customer/<string:customerEmail>")
def find_by_customerEmail(customerEmail):
    customer = Customer.query.filter_by(customerEmail=customerEmail).first()
    if customer:
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404

@app.route("/customer", methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(**data)

    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the customer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": customer.json()
        }
    ), 201


