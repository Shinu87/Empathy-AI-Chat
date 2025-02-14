import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import Message from "./Message";
import { FaPaperPlane } from "react-icons/fa"; // Send Icon

const Chatbot = () => {
  const [messages, setMessages] = useState([]); // Stores entire chat history
  const [input, setInput] = useState("");
  const chatBoxRef = useRef(null);

  useEffect(() => {
    // Auto-scroll to the latest message
    chatBoxRef.current?.scrollTo(0, chatBoxRef.current.scrollHeight);
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessage = { text: input, user: "You" };
    const updatedMessages = [...messages, newMessage];

    setMessages(updatedMessages);

    try {
      const response = await axios.post("http://127.0.0.1:5000/chat", {
        history: updatedMessages, // Send entire conversation
      });

      setMessages([
        ...updatedMessages,
        { text: response.data.response, user: "AI" },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
    }

    setInput("");
  };

  return (
    <>
      <style>
        {`
          .chat-container {
            width: 800px; /* Increased width for longer messages */
            max-width: 95%;
            height: 600px; /* Increased height for better chat visibility */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: #f9f9f9;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            margin: auto;
            font-family: 'Arial', sans-serif;
          }

          .chat-box {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: #aaa transparent;
            word-wrap: break-word; /* Ensure long messages wrap properly */
          }

          .chat-box::-webkit-scrollbar {
            width: 8px;
          }

          .chat-box::-webkit-scrollbar-thumb {
            background-color: #aaa;
            border-radius: 6px;
          }

          .input-container {
            display: flex;
            align-items: center;
            padding: 12px;
            background: white;
            border-top: 1px solid #ddd;
          }

          input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            background: #f1f1f1;
            transition: 0.3s;
            word-wrap: break-word;
          }

          input:focus {
            background: #e8f0fe;
          }

          button {
            margin-left: 10px;
            background: #0078ff;
            color: white;
            border: none;
            padding: 12px 14px;
            border-radius: 50%;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0px 4px 6px rgba(0, 120, 255, 0.3);
          }

          button:hover {
            background: #005ecb;
            transform: scale(1.1);
          }

          .fa-paper-plane {
            font-size: 20px;
          }
        `}
      </style>

      <div className="chat-container">
        <div className="chat-box" ref={chatBoxRef}>
          {messages.map((msg, index) => (
            <Message key={index} text={msg.text} user={msg.user} />
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>
            <FaPaperPlane />
          </button>
        </div>
      </div>
    </>
  );
};

export default Chatbot;
