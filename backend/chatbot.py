import google.generativeai as genai
from sentiment_analysis import analyze_sentiment
from config import GOOGLE_API_KEY
import logging
import time

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_prompt(sentiment, user_input):
    prompts = {
        "very positive": f"🎉 The user is very happy! Show excitement: {user_input}",
        "positive": f"😊 The user is happy. Respond with joy: {user_input}",
        "neutral": f"🤖 The user is neutral. Provide an informative response: {user_input}",
        "negative": f"😞 The user is sad. Respond with care: {user_input}",
        "very negative": f"💔 The user is deeply upset. Be supportive: {user_input}",
    }
    return prompts.get(sentiment, f"🤖 Default response: {user_input}")

def generate_response(user_input):
    sentiment_result = analyze_sentiment(user_input)
    sentiment = sentiment_result["sentiment"]

    chatbot_prompt = get_prompt(sentiment, user_input)
    try:
        response = model.generate_content(chatbot_prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "⚠️ Sorry, I couldn't process your request."

def chatbot_interface():
    print("🤖 Welcome to Empathy Chatbot!")
    print("💬 Type your message below and chat with me.")
    print("🛑 Type 'exit' to end the conversation.")
    
    while True:
        user_message = input("👤 You: ")
        if user_message.lower() == "exit":
            print("👋 Goodbye! Have a great day!")
            break
        chatbot_response = generate_response(user_message)
        print(f"🤖 Chatbot: {chatbot_response}")
        time.sleep(1)

if __name__ == "__main__":
    chatbot_interface()
