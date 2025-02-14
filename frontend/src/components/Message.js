import React from "react";

const Message = ({ text, user }) => (
  <>
    <style>
      {`
        .message {
          max-width: 90%;
          padding: 12px 16px;
          margin: 18px;
          border-radius: 18px;
          font-size: 16px;
          word-wrap: break-word;
          display: flex;
          align-items: center;
          box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
          transition: 0.3s ease-in-out;
        }

        .user {
          background-color: gray;
          color: white;
          align-self: flex-end;
          border-bottom-right-radius: 5px;
          border-top-left-radius: 18px;
        }

        .ai {
          background-color: #f1f1f1;
          color: black;
          align-self: flex-start;
          border-bottom-left-radius: 5px;
          border-top-right-radius: 18px;
        }

        /* Message Animation */
        .message:hover {
          transform: scale(1.02);
        }

        /* Chat Layout */
        .chat-container {
          display: flex;
          flex-direction: column;
          gap: 10px;
          padding: 20px;
        }
      `}
    </style>

    <div className={`message ${user === "AI" ? "ai" : "user"}`}>
      <strong>{user}:</strong> {text}
    </div>
  </>
);

export default Message;
