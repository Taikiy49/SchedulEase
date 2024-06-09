from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    message = data['message']
    print(message)
    response = {'reply': 'Your message was received: ' + message}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
