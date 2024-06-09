import React, { useState, useEffect } from 'react';
import './App.css'; // Import the CSS file for styling

const App = () => {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const sendMessage = async () => {
        if (inputText.trim() === '') return; // Prevent sending empty messages

        // Add the user's message to the UI immediately
        const newMessages = [...messages, { text: inputText, fromUser: true }];
        setMessages(newMessages);
        setInputText(''); // Clear the input field after sending the message

    };

    const handleInputChange = (e) => {
        setInputText(e.target.value); 
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage(); // Send message on Enter key press
        }
    };

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <div className="app-container">
            <div className={`side-menu ${isMenuOpen ? 'open' : ''}`}>
                <div className="hamburger-background">
                    <img 
                        src="hamburger-icon.png" 
                        className={`hamburger ${isMenuOpen ? 'no-background' : ''}`}
                        onClick={toggleMenu}
                        alt="Hamburger Icon"
                    />
                </div>
                
                <div className={`menu-container ${isMenuOpen ? 'open' : ''}`}>
                    <div className="menu"><p>View Schedule</p></div>
                    <div className="menu"><p>SchedulEase</p></div>
                    <div className="menu"><p>Explore</p></div>
                </div>
            </div>

            <div className="chat-container">
                <div className="title-container">
                    <div className="title">SchedulEase</div>
                    <img src="calendar-image.png" className="calendar-image" alt="Calendar" />
                </div>
                <div className="example-options-container">
                    <div className="option">
                        <p>Add</p>
                        <div className="option-description">Add John to the schedule.</div>
                    </div>
                    <div className="option">
                        <p>Remove</p>
                        <div className="option-description">Remove John from the schedule.</div>
                    </div>
                    <div className="option">
                        <p>Constrain</p>
                        <div className="option-description">John cannot work on Friday.</div>
                    </div>
                </div>

                <div className="chat-messages">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.fromUser ? 'user' : 'chatbot'}`}>
                            <p>{msg.text}</p>
                        </div>
                    ))}
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        value={inputText}
                        onChange={handleInputChange}
                        onKeyPress={handleKeyPress}
                        placeholder="Type your message here..."
                    />
                    <button className="input-container-button" onClick={sendMessage}>Send</button>
                </div>
            </div>
        </div>
    );
};

export default App;
