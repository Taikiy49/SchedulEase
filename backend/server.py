from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_settings import ChatbotSettings

app = Flask(__name__)
CORS(app)
chatbot = ChatbotSettings()
chatbot.run_program()

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    message = data['message']
    convo = chatbot._chat_session
    if message.lower() == "quit": 
        return jsonify({"response": "Thank you for using SchedulEase! We'll see you again next time!"})
    convo.send_message(message)
    response = convo.last.text
    if message.lower() == "submit schedule":
        SCHEDULED_STRING = response.strip()
        print(SCHEDULED_STRING)
        if '(' in response and ')' in response:
            return jsonify({"response": "Schedule in terminal"})
        else:
            return jsonify({"response": response})
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
