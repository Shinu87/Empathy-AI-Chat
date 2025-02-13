from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import generate_response

app = Flask(__name__)
CORS(app)  # Allow frontend to access API

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot messages with memory from frontend."""
    conversation_history = request.json.get("history", [])  # Get full history from frontend

    if not conversation_history:
        return jsonify({"error": "Conversation history required"}), 400

    # Keep only the last 10 messages for context
    conversation_history = conversation_history[-10:]

    # Convert conversation history into a single context string
    context = "\n".join([f"{msg['user']}: {msg['text']}" for msg in conversation_history])

    # Generate response using the entire chat history
    bot_response = generate_response(context)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
