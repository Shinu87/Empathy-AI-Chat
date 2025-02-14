import React from "react";
import Chatbot from "./components/Chatbot";
import { FaRobot } from "react-icons/fa"; // AI Robot Icon

const App = () => {
  return (
    <>
      <style>
        {`
          body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
          }

          .App {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            width: 450px;
            max-width: 90%;
          }

          .heading {
            font-size: 28px;
            font-weight: bold;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
            background: black;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }

          .heading-icon {
            font-size: 32px;
            color: orange;
          }
        `}
      </style>

      <h1 className="heading">
        <FaRobot className="heading-icon" /> Empathy AI Chat
      </h1>

      <div className="App">
        <Chatbot />
      </div>
    </>
  );
};

export default App;
