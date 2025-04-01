import random

# List of magic 8 ball answers
magic8_response = ["Yes - definitely",
            "It is decidedly so",
            "Without a doubt",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"]

print("What is your name?")
#need to fill with input variable
print("Present your question:")
#need to fill with input variable
magic8_answer = random.choice(magic8_response)
print(f"Magic 8-Ball’s answer: {magic8_answer}")


