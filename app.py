from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from models import Hero, Power, HeroPower, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "hero_id": hp.hero_id,
                "id": hp.id,
                "power": {"id": hp.power.id, "name": hp.power.name, "description": hp.power.description},
                "power_id": hp.power_id,
                "strength": hp.strength
            } for hp in hero.hero_powers
        ]
    })