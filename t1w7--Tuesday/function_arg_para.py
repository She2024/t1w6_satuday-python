# # Greeting someone
# def greet():
#     print("Hello Coder, Max!")

# greet()

# def greet():
#     print("Hello Coder, Sam!")

# greet()

# #generalised coding 

# def greet(name): #<--- parameter
#     print(f"Hello Coder, {name}!")

# greet("Bob")

# def greetings(fname, lname): #<--- parameter
#     print(f"Hello Coder, {fname} {lname}!")

# greet("Bob", "Brown")

def subtract(a, b):
    difference = a - b
    return difference
result = subtract(4, 3)

print(result)

def subtract(a, b=1): #default or optional parameter
    difference = a - b
    return difference
result = subtract(4, 3)

print(result)

def subtract(a, b=1): #default or optional parameter
    difference = a - b
    return difference
result = subtract(b=4, a=3)

print(result)