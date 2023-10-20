from flask import jsonify, request

from app import app, db
from models import Product

import uuid


# get all products
@app.route("/product")
def get_products():
    product_list = Product.query.all()

    return jsonify({"code": 200, "data": [product.json() for product in product_list]})


@app.route("/product/create", methods=["POST"])
def create_product():
    data = request.get_json()
    product = Product(Product_ID=uuid.uuid5(), **data)
    product_name = product.Product_Name

    if Product.query.filter_by(Product_Name=product_name).first():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "message": "Product created",
                },
            },
            200,
        )

