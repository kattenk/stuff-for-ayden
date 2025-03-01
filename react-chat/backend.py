from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from dataclasses import dataclass

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@dataclass
class Message:
    id: int
    name: str
    text: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "text": self.text
        }

messages = []

@socketio.on('connect')
def handle_connect():
    print("New client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def new_message():
    data = request.get_json()

    new_message = Message(
        id=len(messages),
        name=data["name"],
        text=data["text"]
    )

    messages.append(new_message)
    socketio.emit('new_message', new_message.to_dict())
    
    return jsonify(new_message.to_dict()), 201

socketio.run(app, host="0.0.0.0", port=5000, debug=True)