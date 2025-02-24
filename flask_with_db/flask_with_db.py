from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_key'

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def view_list():
    return render_template("list.jinja", items=Item.query.all())

@app.route("/new-item", methods=["POST"])
def new_item():
    db.session.add(Item(
        text=request.form.get("new_item")
    ))

    db.session.commit()

    return redirect(url_for("view_list"))

@app.route("/remove-item/", methods=["POST"])
def remove_item():
    db.session.delete(Item.query.get(int(request.form.get("id"))))
    db.session.commit()
    
    return redirect(url_for("view_list"))

app.run(debug=True)
