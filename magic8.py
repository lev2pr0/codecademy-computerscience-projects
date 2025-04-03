import random

# List of Magic 8 ball's answers
magic8_response = ["Yes - definitely",
            "It is decidedly so",
            "Without a doubt",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"]

# Magic 8 ball Program Welcome
print("Welcome to the Magic 8-Ball!" + "\n")

# Ask for user's name and question
print("What is your name?" + "\n")
name = input("What is your name? ")
print("Hello " + name + "!" + "\n")
print("Ask me a yes or no question, and I will give you an answer." + "\n")
question = input("What is your question? ")

# Print the user's question
print(f"{name}, asks: {question}\n")

# Generate a random answer from the Magic 8 ball
magic8_answer = random.choice(magic8_response)
print(f"Magic 8-Ball’s answer: {magic8_answer}")


