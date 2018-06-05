from flask import Flask
from json import loads, dumps
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
app.debug = True
socketio = SocketIO(app)


@socketio.on('connected')
def new_connection(data):
    print("A new client has connected!")
    emit('respond', {'data': 'Thanks for connecting'})


@socketio.on('attention')
def get_attention(data):
    print("I WANT ATTENTION")


if __name__ == '__main__':
    socketio.run(app)
