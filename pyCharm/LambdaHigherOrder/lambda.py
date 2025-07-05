# Single expresions that return all values
squared = lambda num : num * num 
# def squared(num): return num * num # non-lambda function
print(squared(3))

twoNumbers = lambda num : num + 2
# def twoNumbers(num): return num + 2 # non-lambda function
print(twoNumbers(2))

sum = lambda a, b : a + b
# def sum(a, b): return a + b # non-lambda function
print(sum(2, 3))

# Higher order function
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(13))


##########
numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

##########
odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

##########
from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

names = ["Miguel Gonzalez", "Sara Ito", "John Jacob Jingleheimerschmidt"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)
