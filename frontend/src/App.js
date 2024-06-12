import React, { useState } from 'react';
import './App.css';
import ChatContainer from './ChatContainer';
import SideMenu from './SideMenu';

const App = () => {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const sendMessage = async () => {
        if (inputText.trim() === '') return;

        const newMessages = [...messages, { text: inputText, fromUser: true }];
        setMessages(newMessages);
        setInputText('');
        
        const response = await fetch('http://127.0.0.1:5000/send-message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: inputText }),
        });

        const responseData = await response.json();
        setMessages([...newMessages, { text: responseData.response, fromUser: false }]);
    };

    const handleInputChange = (e) => {
        setInputText(e.target.value); 
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <div className="app-container">
            <SideMenu isMenuOpen={isMenuOpen} toggleMenu={toggleMenu} />
            <ChatContainer
                messages={messages}
                inputText={inputText}
                handleInputChange={handleInputChange}
                handleKeyPress={handleKeyPress}
                sendMessage={sendMessage}
            />
        </div>
    );
};

export default App;
