class JustNotCoolError(Exception):
    pass # It receive an specific message

x = input(f"\nHi, please introduce some value between 1 and 10...")
try:
    raise JustNotCoolError("This just isn't a cool error!") # Call the class and introduce the message by error
    # raise Exception("I'm a custom exception!")    
    # print(int(x) / 2)

    if not type(x) is str:
        raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError: maybe something is used but not defined')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error")