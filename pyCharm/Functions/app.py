# defining functions in Python

# def greet(name): # name is a parameter
#     """Function to greet a person with their name.""" # docstring
#     # This function prints a greeting message
#     print(f"Hello, {name}!") # f string for formatting

# greet("Alice") # calling the function with an argument

# types of parameters
# def get_greeting(name):
#     """Function to greet a person with a custom greeting."""
#     return f" {name}!" # f string for formatting

# print(get_greeting("Alice")) # calling the function with an argument and printing the result, resulting in " Alice!"

# message = get_greeting("Alice") # calling the function with an argument
# file = open("content.txt", "w") # opening a file in write mode
# file.write(message) # writing the message to a file

# incrementing a number by a specified value
# This function takes a number and an increment value, adds them, and returns the result.
# def increment(number, by):
#     """Function to increment a number by a specified value."""
#     return number + by  # returns the incremented value

# result = increment(2, 1)  # calling the function with arguments, resulting in 3
# print(result)  # printing the result, which is 3

# default parameters
# def increment(number, by=1):
#     """Function to increment a number by a specified value, defaulting to 1."""
#     return number + by  # returns the incremented value

# print(increment(2))  # calling the function with one argument, resulting in 3
# print(increment(2, 5))  # calling the function with one argument, resulting in 3

# args, what, wait
# def multiply(x, y): # just two parameters
# def multiply(*numbers):
#     """Function to multiply two numbers."""
#     # print(numbers)  # prints the tuple of numbers passed to the function
#     # return x * y  # returns the product of x and y
#     total = 1 # initializing total to 1 for multiplication
#     for number in numbers:
#         # total = total * number # multiplying each number in the tuple
#         total *= number  # updating total with the product
#     return total # in this position, total is out of the loop, so it returns the final product

# print(multiply(2, 3, 4, 5))  # calling the function with three arguments, but it only takes two
# This will raise a TypeError because the function expects exactly two arguments.

# ejercicio: crea una función que reciba diccionarios con nombres, edaddes yu que defina la mayor edad
# def find_oldest_person(people):
#     """Function to find the oldest person in a dictionary of names and ages."""
#     oldest_person = None # Initialize oldest_person to None
#     max_age = 0 # Initialize max_age to 0
#     state = None # Initialize state to None

#     for person in people:  # Iterate through the dictionary of people
#         # take person info from each people
#         name = person["name"] # Get the name of the person
#         age = person["age"] # Get the age of the person
#         is_student = person["is_student"] # Get the student's status of the person

#         if age > max_age:  # Check if the current age is greater than max_age
#             max_age = age  # Update max_age
#             oldest_person = name # Update oldest_person
#             state = "is a student" if is_student else "is not a student"  # check if the person is a student or not

#     return oldest_person, max_age, state  # Return the name and age of the oldest person

# # Example usage
# people = [
#     {
#         "name": "Alice",
#         "age": 30,
#         "is_student": True
#     },
#     {
#         "name": "Bob",
#         "age": 25,
#         "is_student": False
#     },
#     {
#         "name": "Charlie",
#         "age": 35,
#         "is_student": True
#     },
#     {
#         "name": "Diana",
#         "age": 28,
#         "is_student": False
#     }
# ]
# oldest_person, age, state = find_oldest_person(people)  # Calling the function with a dictionary of names and ages
# print(f"The oldest person is {oldest_person} with age {age}, and {state}.")  # Output: The oldest person is Charlie with age 35.

# split emojis
message = input("> ")
words = message.split(" ")  # Split the message into words
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😄",
    ":P": "😛",
    ":o": "😮",
    ":|": "😐",
    ":/": "😕",
    ":*": "😘",
    ";)": "😉",
    ":3": "😺",
    ":'(": "😢",
    ":$": "😳",
    ":@": "😠",
    ":&": "😖",
    ":!": "😲",
    ":^": "😏",
}

# Replace emojis in the words list
output = ""
for word in words:
    output += emojis.get(word, word) + " "  # Use the emoji if it exists, otherwise use the word itself
print(output)  # Print the list of words