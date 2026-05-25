# Rule-Based AI Chatbot

print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

# Dictionary of responses
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "I am an AI chatbot.",
    "who created you": "I was created using Python.",
    "bye": "Goodbye! Have a nice day!"
}

# Infinite loop
while True:

    # Taking user input
    user_input = input("You: ")

    # Input sanitization
    clean_input = user_input.lower().strip()

    # Exit condition
    if clean_input == "bye":
        print("Bot:", responses["bye"])
        break

    # Get response from dictionary
    reply = responses.get(clean_input,
                          "Sorry, I don't understand that.")

    print("Bot:", reply)