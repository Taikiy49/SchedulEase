import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Import the CSS file for styling

const App = () => {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');

  useEffect(() => {
    // Function to fetch initial messages from the chatbot when the component mounts
    fetchInitialMessages();
  }, []);

  const fetchInitialMessages = async () => {
    try {
      // Make an HTTP request to fetch initial messages from the chatbot service
      const response = await axios.get('YOUR_CHATBOT_API_ENDPOINT');
      setMessages(response.data.messages); // Assuming the response contains an array of messages
    } catch (error) {
      console.error('Error fetching initial messages:', error);
    }
  };

  const sendMessage = async () => {
    try {
      // Make an HTTP request to send a message to the chatbot service
      const response = await axios.post('YOUR_CHATBOT_API_ENDPOINT', { message: inputText });
      const newMessages = [...messages, { text: inputText, fromUser: true }, { text: response.data.text, fromUser: false }];
      setMessages(newMessages); // Update the messages array with both user and chatbot messages
      setInputText(''); // Clear the input field after sending the message
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value); // Update the inputText state as the user types
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {/* Render the messages */}
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.fromUser ? 'user' : 'chatbot'}`}>
            <p>{msg.text}</p>
          </div>
        ))}
      </div>
      <div className="input-container">
        {/* Input field for sending messages */}
        <input type="text" value={inputText} onChange={handleInputChange} />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default App;
