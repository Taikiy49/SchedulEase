from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_settings import ChatbotSettings

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
chatbot = ChatbotSettings()
chatbot.run_program()

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    message = data['message']

    convo = chatbot._chat_session
    convo.send_message(message)
    response = convo.last.text
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
