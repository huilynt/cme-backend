from app import db


class Product(db.Model):
    __tablename__ = "product"
    Product_ID = db.Column(db.Integer, primary_key=True)
    Product_Name = db.Column(db.String(20), nullable=False)
    Product_Qty = db.Column(db.Integer, primary_key=False)
    Product_Price = db.Column(db.Double, primary_key=False)
    Product_Description = db.Column(db.String(255), primary_key=False)
    Product_StockAvailable = db.Column(db.Boolean, primary_key=False)

    def __init__(self, Product_ID, Product_Name):
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name

    def json(self):
        return {"Product_ID": self.Product_ID, "Product_Name": self.Product_Name}
