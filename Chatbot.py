import nltk
from nltk.chat.util import Chat, reflections

# You can expand these pairs with more patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm fine, thank you. How can I assist you today?"]],
    [r"what is your name?", ["I'm ChatBot, your virtual assistant."]],
    [r"what can you do?", ["I can chat with you, answer simple questions, and keep you company."]],
    [r"who created you?", ["I was created by a Python programmer."]],
    [r"(.*) your favorite (.*)", ["I don't have preferences, but I like helping humans!"]],
    [r"quit|exit", ["Goodbye! Have a nice day.", "See you later!"]],
    [r"(.*)", ["Interesting... Tell me more.", "Hmm... I see.", "Let's talk about something else."]]
]

def chatbot():
    print("🤖 ChatBot: Hello! I'm a basic chatbot. Type 'quit' or 'exit' to end the chat.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
