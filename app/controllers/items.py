from app import app, db
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models.item import Item

class ItemRoutes:
    @app.route("/items")
    def get_items():
        try:
            items=Item.query.all()
            return jsonify([e.serialize() for e in items])
        except Exception as e:
            return(str(e))

    @app.route("/items/<id_>")
    def get_item(id_):
        try:
            item=Item.query.filter_by(id=id_).first()
            return jsonify(item.serialize())
        except Exception as e:
            return(str(e))