from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_key'

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
CORS(app)

class Item(db.Model):
    text = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text
        }

with app.app_context():
    db.create_all()

@app.route('/items', methods=['GET'])
def get_items():    
    return jsonify([item.to_dict() for item in Item.query.all()])

@app.route('/items', methods=['POST'])
def new_item():    
    data = request.get_json()
    
    new_item = Item(text=data['text'])
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify(new_item.to_dict()), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def remove_item(item_id):
    db.session.delete(Item.query.get(int(item_id)))
    db.session.commit()
    
    return "", 200

app.run(debug=True)