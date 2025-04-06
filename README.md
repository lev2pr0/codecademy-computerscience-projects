# Codecademy Computer Science 
`Details of the Computer Science projects and what was learned`

**Important Note:** Portfolio projects referenced will have its own repository linked instead of file itself

## Intro to Programming

### Introduction to the Computer Science Career Path
- **Block Letters - [blockletter.py](https://github.com/lev2pr0/codecademy-computerscience-projects/blob/main/blockletter.py)**

`Display my initials on screen in block characters to create an ASCII art.`

*Learned how to use store rows of strings in variables and display ASCII art initials using loop*
<br><br/>
- **Receipts for Lovely Loveseats - [LovelyseatsReceipts.py](https://github.com/lev2pr0/codecademy-computerscience-projects/blob/main/LovelyseatsReceipts.py)**
  
`Keep receipts for your lovely loveseats. Programming is a treat with this sweet suite of feats! Use strings and numbers to save a catalog of furniture, then perform concatenation and math calculations to create a receipt.`

*Learned how to work with multiple variables to perform concatenation and calculations to create a printed receipt. Additionally, this project forced me to organize code and use clear variables for legibility and performance.*
<br><br/>
- **Magic 8-Ball - [magic8.py](https://github.com/lev2pr0/codecademy-computerscience-projects/blob/main/magic8.py)**
  
`Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes. We’ll be using the following 9 possible answers for our Magic 8-Ball:`

```python
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
```
*I learned how to use ```import random``` module and the difference between ```random.randint()``` (random integer from specified range) and ```random.choice()``` (random element within a sequence like list, tuple, or string) functions. AI's code review showed how I can write readable code using f-string in this project. Lastly, the codecademy version I had to save to complete assessment had me use ```if/elif/else``` statements in place of variable with stored strings to use ```random.randint()``` to randomize based on number generated; this version of project is [magic8_v2](https://github.com/lev2pr0/codecademy-computerscience-projects/blob/main/magic8_v2.py)*
<br><br/>
- **Sal's Shipping - [shipping.py](https://github.com/lev2pr0/codecademy-computerscience-projects/blob/main/shipping.py)**

`In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.`
`Sal’s Shippers has several different options for a customer to ship their package:`

```python
# Ground shipping cost calculation
def calculate_ground_shipping(weight):
    if weight <= 2:
        return weight * 1.50 + 20
    elif weight <= 6:
        return weight * 3.00 + 20
    elif weight <= 10:
        return weight * 4.00 + 20
    else:
        return weight * 4.75 + 20

if weight > 0:
    ground_shipping_cost = calculate_ground_shipping(weight)
    print("Ground Shipping $", ground_shipping_cost)
else:
    ground_shipping_cost = float('inf')  # Set to infinity to exclude from comparison

# Ground shipping premium cost calculation
ground_premium_cost = 125.00
print("Ground Shipping Premium $", ground_premium_cost)

# Drone shipping cost calculation
def calculate_drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

if weight > 0:
    drone_shipping_cost = calculate_drone_shipping(weight)
    print("Drone Shipping $", drone_shipping_cost)
else:
    drone_shipping_cost = float('inf')  # Set to infinity to exclude from comparison
```

This project was more practice with ```if/elif/else``` statements. I learned how to use ```def``` to define function for efficiency, ```weight = float(input("Enter the package weight: "))``` for user inputs, and always including error handling for invalid entries using ```try``` statement.
<br><br/>

### Fundamentals of Python

<br><br/>
## Intro to Data Structures

<br><br/>
## Algortithms 

<br><br/>
## Trees and Graphs

<br><br/>
## Databases

<br><br/>
## Computer Architecture 

<br><br/>
## Math for Computer Science


