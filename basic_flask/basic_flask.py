from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = []

@app.route("/", methods=["GET"])
def view_list():    
    return render_template("list.jinja", items=list(enumerate(items)))

@app.route("/new-item", methods=["POST"])
def new_item():
    items.append(request.form.get("new_item"))

    return redirect(url_for("view_list"))

@app.route("/remove-item/", methods=["POST"])
def remove_item():
    items.pop(int(request.form.get("index")))

    return redirect(url_for("view_list"))

app.run(debug=True)
