import React from 'react';

const ChatContainer = ({ messages, inputText, handleInputChange, handleKeyPress, sendMessage }) => (
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
);

export default ChatContainer;
