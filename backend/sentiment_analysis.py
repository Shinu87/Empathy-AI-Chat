import re
import logging
from collections import Counter, deque
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load RoBERTa Sentiment Model
sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Conversation Memory (Stores Last 5 Messages)
chat_memory = deque(maxlen=5)

def preprocess_text(text):
    """Preprocess text by removing URLs, special characters, and extra spaces."""
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)  # Remove special characters
    return text.strip()

def extract_keywords(text, top_n=5):
    """Extract important keywords using frequency analysis."""
    words = text.split()
    word_freq = Counter(words)
    return [word for word, freq in word_freq.most_common(top_n)]

def analyze_sentiment(text):
    """Analyzes sentiment using RoBERTa and extracts relevant information."""
    if not isinstance(text, str) or not text.strip():
        return {"sentiment": "neutral", "confidence": 0.0, "keywords": []}

    text = preprocess_text(text)
    result = sentiment_model(text)[0]
    label, score = result['label'], result['score']

    # Map RoBERTa Labels to Custom Categories
    if label == "LABEL_2" and score > 0.6:
        sentiment = "very positive"
    elif label == "LABEL_2":
        sentiment = "positive"
    elif label == "LABEL_1":
        sentiment = "neutral"
    elif label == "LABEL_0" and score > 0.6:
        sentiment = "very negative"
    else:
        sentiment = "negative"

    # Extract Important Keywords
    keywords = extract_keywords(text)

    logging.info(f"Analyzed sentiment: {text} -> {sentiment}")

    return {
        "sentiment": sentiment,
        "confidence": round(score, 2),
        "keywords": keywords
    }

def generate_response(user_input):
    """Generates chatbot responses based on sentiment and conversation memory."""
    sentiment_result = analyze_sentiment(user_input)
    sentiment = sentiment_result["sentiment"]
    
    # Update Chat Memory
    chat_memory.append(f"User: {user_input} | Sentiment: {sentiment}")

    # Define Response Prompts
    prompt_map = {
        "very positive": "The user is extremely happy! Respond with enthusiasm and excitement.",
        "positive": "The user is happy. Respond cheerfully.",
        "neutral": "Respond in a neutral and informative way.",
        "negative": "The user is feeling down. Respond with empathy and support.",
        "very negative": "The user is very upset. Respond with deep understanding and reassurance.",
    }

    chatbot_prompt = "\n".join(chat_memory) + f"\nChatbot: {prompt_map.get(sentiment, 'Respond naturally')}"

    logging.info(f"Generated chatbot response for sentiment: {sentiment}")
    return chatbot_prompt

# Example Usage
if __name__ == "__main__":
    sample_texts = [
        "I absolutely love this chatbot! 😊 It's the best thing ever!",
        "This service is terrible... I hate it!",
        "The experience was okay, nothing special.",
        "I'm feeling a bit down today. Not sure why. 😞",
        "Such an amazing event! Had a wonderful time 🎉."
    ]

    for text in sample_texts:
        result = analyze_sentiment(text)
        response = generate_response(text)
        print(f"Input: {text}\nAnalysis: {result}\nResponse: {response}\n{'-'*50}")
