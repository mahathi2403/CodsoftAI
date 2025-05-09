def chatbot_response(user_input):
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."
    elif "help" in user_input:
        return "Sure, I'm here to help. Please tell me your question."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Main chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
