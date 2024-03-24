import random
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
# nltk.download('punkt')

# A dictionary of responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I assist you today?"],
    "how are you": ["I'm just a bot, but I'm functioning well. How can I assist you?",
                    "I'm doing fine, thank you for asking. What can I do for you?"],
    "what's your name": ["I'm a bot, but you can call me ChatBot.", "I go by the name ChatBot."],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Farewell! Come back anytime."],
    "time": ["I don't have a watch, but you can check the time on your device!",
             "Time is a concept I'm not familiar with, sorry!"],
    "weather": [
        "I'm afraid I can't provide real-time weather updates. You might want to check a weather website or app.",
        "I don't have access to weather data, but you can easily find it online."],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "age": ["I'm just a bot, so I don't have an age.", "I'm ageless, like a digital immortal."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!",
             "I told my wife she was drawing her eyebrows too high. She looked surprised.",
             "Why don't skeletons fight each other? They don't have the guts."],
    "creator": ["I was created by Zaky Ahamed. He's a talented programmer!", "My creator is Zaky Ahamed. He's pretty awesome."],
    "default": ["I'm not sure I understand. Can you rephrase that?", "I'm sorry, I didn't get that."]
}

# A list of greetings to start the conversation
greetings = ["hi", "hello", "hey"]


def chatbot_response(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input.lower())

    # Check if the user input is a greeting
    if any(word in tokens for word in greetings):
        return random.choice(responses["hello"])

    # Check if the user input matches any predefined responses
    for key, value in responses.items():
        if any(word in tokens for word in key.split()):
            return random.choice(value)

    # If no match is found, return a default response
    return random.choice(responses["default"])


def chatbot():
    print("Hello, I'm a bot. How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break
        elif "who created you" in user_input.lower():
            print("Chatbot:", random.choice(responses["creator"]))
        else:
            print("Chatbot:", chatbot_response(user_input))


# Run the chatbot
chatbot()