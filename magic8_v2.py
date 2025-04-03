import random

# Determine the Magic 8 ball's answer based on a random number
random_number = random.randint(1,9)
if random_number == 1:
  magic8_answer = "Yes-definitely"
elif random_number == 2:
  magic8_answer = "It is decidedly so"
elif random_number == 3:
  magic8_answer = "Without a doubt"
elif random_number == 4:
  magic8_answer = "Reply hazy, try again"
elif random_number == 5:
  magic8_answer = "Ask again later"
elif random_number == 6:
  magic8_answer = "Better not tell you now"
elif random_number == 7:
  magic8_answer = "My sources say no"
elif random_number == 8:
  magic8_answer = "Outlook not so good"
elif random_number == 9:
  magic8_answer = "Very doubtful"
else:
  magic8_answer = "Error"

# Magic 8 ball Program Welcome
print("Welcome to the Magic 8-Ball!\n")

# Ask for user's name, question, and provide answer
name = "Lev"
question = "Question?"

if question == "":
  print("Please ask a yes or no question." + "\n")
elif name == "":
  print(f"Question: {question}\n")
  print(f"Magic 8-Ball’s answer: {magic8_answer}")
else:
  print(f"Hello {name}!" + "\n")
  print("Ask me a yes or no question, and I will give you an answer." + "\n")
  print(f"{name}, asks: {question}\n")
  print(f"Magic 8-Ball’s answer: {magic8_answer}")