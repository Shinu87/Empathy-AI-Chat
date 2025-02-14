# 🤖 Empathy AI Chat

An advanced AI chatbot that understands user emotions and provides empathetic, context-aware responses. This project enhances chatbot interaction by tracking emotional trends, offering actionable advice, and maintaining short-term memory for meaningful conversations.

## 📌 Features

✅ **Emotion Detection** - Identifies user sentiment and tailors responses accordingly.  
✅ **Memory for Contextual Conversations** - Remembers previous interactions in a session for better replies.  
✅ **Diverse Response Variations** - Avoids repetitive messages by using multiple response patterns.  
✅ **Action-Oriented Advice** - Provides practical steps instead of just emotional support.  
✅ **Natural Conversational Flow** - Uses human-like language for a more engaging experience.  

## **⚡ Complex Prompt Showcase (Model Accuracy)**
The chatbot can handle **deep emotional conversations** with **context awareness**, **subtle sentiment detection**, and **empathetic responses**.  

### **Example 1: Mixed Emotions**
#### **User:**  
_"I'm really proud of myself for finally standing up to my toxic boss, but I also feel a bit guilty... I hope I didn't overreact."_  

---

### **Example 2: Highly Negative Situation**
#### **User:**  
_"I feel like everything is falling apart. I lost my job, my best friend moved away, and I don't know how to cope anymore."_  

---

### **Example 3: Sarcasm & Subtle Sentiment**
#### **User:**  
_"Wow, today was just AMAZING. Everything went wrong, my car broke down, and I spilled coffee on my laptop. Best day ever! 😡"_  

---

💡 **Why This Matters:**  
- The chatbot **accurately understands nuanced emotions** like **mixed feelings, distress, and sarcasm**.  
- It provides **contextually relevant responses** instead of generic replies.  
- Uses **RoBERTa-based sentiment analysis** to handle **complex emotional expressions**.  

📌 *See screenshots below for real-time examples!*  
![WhatsApp Image 2025-02-14 at 02 43 19_fad8dc16](https://github.com/user-attachments/assets/9fd30fdf-f33f-4625-affd-c1d91cb06179)
![WhatsApp Image 2025-02-14 at 02 41 56_318d9a36](https://github.com/user-attachments/assets/ab2d5fc4-7915-443c-a782-41f58db20a97)
![WhatsApp Image 2025-02-14 at 02 45 08_4d39871d](https://github.com/user-attachments/assets/b9c90016-63c7-4fbe-9d05-3e7323e51d84)


"I'm really proud of myself for finally standing up to my toxic boss, but I also feel a bit guilty... I hope I didn't overreact."
## 💡 How It Works
1. The chatbot **detects user emotions** based on input.
2. It **selects the most appropriate response** using NLP models.
3. If the user repeatedly shares similar emotions, it **adjusts its tone** dynamically.
4. The chatbot **remembers previous messages** (within a session) to improve contextual responses.

## 🛠️ Tech Stack
- **Programming Language**: Python 🐍
- **NLP Model**: Google Gemini🤖
- **Framework**: Flask (for deployment) 🌍
- **Memory Management**: Session-based short-term memory 🧠

# 🚀 Chatbot API Key Configuration

## 🔑 Setting Up API Key

To use the chatbot with external APIs (e.g., NLP models, sentiment analysis, or cloud-based services), you need to **configure an API key**.

### 📌 Steps to Configure the API Key

#### 1️⃣ Add the API Key in `config.py`
Ensure that the **`config.py`** file exists in the root directory and contains the following:

```python
# config.py

#Google Gemini API Key
GOOGLE_API_KEY = "your-gemini-api-key-here"
# ⚠️ Important: Do not share this key publicly! Keep it safe and do not commit it to Git.

## 💖 Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push them.
4. Open a Pull Request.


