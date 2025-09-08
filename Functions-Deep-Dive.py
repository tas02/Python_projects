# #functions deep dive

# def greet(name, age):
#     print(f"Hello, {name}! you're {age} years old.")
    
# greet("Alice", 25)

# def describe_pet(animal, name):
#     print(f"I have a {animal} named {name}.")
    
#     describe_pet("dog", "Buddy")
# describe_pet("cat", "Whiskers")
# describe_pet(name="Mittens", animal="cat")
# describe_pet(animal="parrot", name="Polly")
# describe_pet("hamster", name="Nibbles")
# #describe_pet(name="Goldie", "fish")  # This will raise a SyntaxError

#deafult parameters
def add_item(item, list=[]):
    list.append(item)
    return list

print(add_item("apple"))  # Output: ['apple']
print(add_item("banana"))  # Output: ['apple', 'banana']
print(add_item("orange", ["kiwi"]))  # Output: ['kiwi', 'orange']


#return statement

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(3, 5)
# print(result)  # Output: 8

# def get_user_info():
#     return "Alice", 30, "New York"

# name, age, city = get_user_info()

# print(f"Name: {name}, Age: {age}, City: {city}")


# def divide(a, b):
#     if b == 0:
#         return None or "Error: Division by zero"

#     return a / b

# print(divide(10, 2))  # Output: 5.0
# print(divide(10, 0))  # Output: None or "Error: Division by zero"
# print(divide(10, 3))  # Output: 3.3333333333333335

# def greet(name):
#     print(f"Hello, {name}!")
    
#     result = greet("Bob")  # Output: Hello, Bob!
#     print(result)  # Output: None
    
    
    #docstring
    
def calculate_area(length, width):
        """
    Calculate the area of a circle given its radius.
        
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    returns:
    float: The area of the rectangle.
        """
        return length * width
    
print(calculate_area.__doc__)

#first class objects in functions

def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!
print(greet("Bob"))  # Output: Hello, Bob!


def apply_operation(a, b, operation):
    return operation(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(apply_operation(5, 3, add))       # Output: 8
print(apply_operation(5, 3, multiply))  # Output: 15

#annonymous functions (lambda)

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

#filter function and iterables  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#map function

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#recursive function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

#decorators

def my_decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()  # Output:
# Before the function call.
# Hello!
# After the function call.
#closure
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function
hi_func = outer_function("Hi!")
hi_func()  # Output: Hi!
hello_func = outer_function("Hello!")
hello_func()  # Output: Hello!

#args and kwargs

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(5, 10, 15, 20))  # Output: 50

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
print_info(product="Laptop", price=999.99, stock=50)
# Output:
# product: Laptop
# price: 999.99
# stock: 50

#generator functions

def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)
    
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
counter = infinite_sequence()

print(next(counter))  # Output: 0   
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

     

