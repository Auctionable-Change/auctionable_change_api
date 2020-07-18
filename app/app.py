from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Item

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/items")
def get_items():
    return "items : {}".format(item)

if __name__ == '__main__':
    app.run()
