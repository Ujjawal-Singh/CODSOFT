import re
def simple_animal_chatbot(user_input):
    user_input = user_input.lower() 

    patterns = {
        r".*hello.*|hey.*|hii.*": "Hello!I'm the animal information chatbot. How can I assist you?",
        r".*bye.*": "Goodbye!Don't hesitate to return if you have more questions in the future",
        r".*what.*your.*name.|who are you.*": "I'm here to provide information about different animals.Feel free to ask me any questions you have.",
        r".*tell.*about.*dog.*": "Dogs are loyal and friendly animals.They come in various breeds",
        r".*tell.*about.*cat.*": "Cats are independent animals that have been domesticated for thousands of years.They are skilled hunters and have unique behaviors.",
        r".*tell.*about.*elephant.*": "Elephants are large mammals known for their intelligence and social behavior.They are large mammals found in different parts of the world.",
        r".*tell.*about.*dolphin.*": "Dolphins are highly intelligent marine mammals that are known for their playful nature.They are known for their problem-solving abilities and playful behavior.",
        r".*thank.*you.*|.*thanks.*": "You're welcome!Feel free to ask if you have more questions.",
        r".*": "I'm sorry,I don't have information on that topic."
    }
    for pattern, response in patterns.items():
        if re.match(pattern, user_input):
            return response
        
print("Chatbot: Hello! I'm the animal information chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = simple_animal_chatbot(user_input)
    print("Chatbot:", response)