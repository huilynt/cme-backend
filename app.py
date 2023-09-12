from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)


@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()