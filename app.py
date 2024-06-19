from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Store received data in a deque with a maximum length
data_store = deque(maxlen=10)


@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    usb_data = data.get('byte_data')
    
    print(f"Received data -  {usb_data}")
    data_store.append({'usb_data': usb_data})
    return jsonify({"status": "success", "data": data}), 200

@app.route('/')
def index():
    return render_template('index.html', data=list(data_store))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
