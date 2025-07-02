# for loops
# for item in "python":
#     print(item) # loop through each character in the string

# for item in [1, 2, 3, 4, 5]:
#     print(item) # loop through each item in the list

# for item in range(10):
#     print(item) # loop through each number in the range from 0 to 9

# for item in range(5, 10):
#     print(item) # loop through each number in the range from 5 to 9

# for item in range(5, 10, 2):
#     print(item) # loop through each number in the range from 5 to 9

# Ejercicio: Crear una lista de tareas y recorrerla con un bucle
# tasks = ["TODO list", "Learn Python", "Learn JavaScript", "Learn C++", "Learn Java"]

# for task in tasks:
#     print(task)  # loop through each task in the list

# while tasks:
#     print(tasks.pop(0))  # remove the first task from the list and print it
#     if not tasks:  # check if the list is empty
#         print("All tasks completed!")
#         break  # exit the loop when all tasks are completed

# Ejercicio: Crea una lista de precios y recorrelo sumando al total
# prices = [10.99, 5.49, 3.99, 12.50, 7.25]
# total = 0

# for price in prices:
#     total += price  # add each price to the total
#     print(f"Current price: {price}, Total so far: {total}")

# nested loops
# for x in range(4):
#     for y in range(3):
#         print(f"x: {x}, y: {y}")  # loop through each combination of x and y

# challenge: Crear un programa que imprima x con bucle anidado for, el caso externo lleva 4 y el interno 2
# numbers = [5 , 2, 5, 2, 2]

# for item in numbers:
#     output = ""
#     for count in range(item):  # loop through the range of the current item
#         output += "x"
#     print(output)  # print the output for the current item

# Lists
# names = ["Alice", "Bob", "Charlie", "David"]
# print(names)
# print(names[0])  # Access the first item in the list
# print(names[1:3])  # Access a slice of the list (items at index 1 and 2)
# print(names[-1])  # Access the last item in the list
# print(names[-2:])  # Access the last two items in the list
# print(names[:2])  # Access the first two items in the list
# print(names[1:])  # Access all items starting from index 1
# print(names[:])  # Access all items in the list
# print(f"Names: {names[:]}")

# Ejercicio: Crea un programa que busque el número más grande en una lista de números
# numbers = [10, 5, 8, 48, 12, 3]
# max_number = numbers[0]  # Start with the first number as the maximum
# for number in numbers:
#     if number > max_number:  # Check if the current number is greater than the current maximum
#         max_number = number  # Update the maximum number
# print(f"The largest number is: {max_number}")  # Print the largest number found

# 2D Lists
# matrix = [ 
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9] 
# ]

# # Accessing elements in a 2D list
# # print(matrix[0][0])  # Access the first element in the first row
# for row in matrix:
#     for item in row:
#         print(item, end=" ")  # Print each item in the row
#     print()  # Print a new line after each row

# unpacking lists
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpack the tuple into variables
print(x * y * z)