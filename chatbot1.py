def simple_chatbot(user_input):
    rules = {
        'hi|hello|hey': 'Hello! How can I help you?',
        'how are you': 'I am a robo, but thanks for asking!',
        'what is your name': 'I am a simple chatbot.',
        'bye|goodbye': 'Goodbye! Have a great day!',
        'how do you do|what\'s up|sup': 'Not much, just here to assist you.',
        'tell me a joke|say something funny': 'Why don\'t scientists trust atoms? Because they make up everything!',
        'thank you|thanks': 'You\'re welcome!',
        'help|assistance': 'I can help with general information, jokes, and more. Just ask!',
        'what time is it|current time': 'I\'m sorry, I don\'t have the ability to provide real-time information.',
        'what can you do': 'I can provide information, tell jokes, and engage in basic conversation. Feel free to ask anything!',
        'tell me about yourself': 'I am a simple chatbot designed to assist users with various queries.'
    }

    for pattern, response in rules.items():
        keywords = pattern.split('|')
        for keyword in keywords:
            if keyword in user_input.lower():
                return response

    return "I'm sorry, I didn't understand that."

# Main loop for chatting
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
