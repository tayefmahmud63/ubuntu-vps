from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    # Emit data to all connected clients
    socketio.emit('new_data', data)
    return jsonify(status='success'), 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
