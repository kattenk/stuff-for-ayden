![GIF](todos.gif)
this repo contains the source code for a to-do list application written in three different ways:

# Basic Flask
Uses Jinja templates, HTML forms, and a Python list for storing the todo items, it doesn't use a database, and thus the list items don't stay when the app shuts down.
# Flask with DB
Adds a database, using the [`flask-sqlalchemy`](https://flask-sqlalchemy.readthedocs.io/en/stable/) package, which uses SQLAlchemy, which is an [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) for Python,
otherwise it is the same as the basic flask demo.
# React with REST
a React-based JavaScript frontend that hooks up to a Flask-based Python backend, the frontend and backend use an API written in REST fashion to communicate, and items are stored in a database as before.
