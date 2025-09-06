#Dictionaries - Key-Value Pairs
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 202
# }
# print(thisdict)

# fruits = [("apple", "green"), ("banana", "yellow"), ("orange", "orange"), ("grapes", "purple")]
# fruits= dict(fruits)
# print(fruits)

# characters = {
#   "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(characters)

# student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student["name"])
# print(student["courses"])
# print(student.get("age"))

# # print(student["phone"]) # this will raise an error if the key does not exist
# print(student.get("phone")) # this will return None if the key does not exist   

# print(student.get("phone", "Not Found")) # this will return "Not Found" if the key does not exist
# print(student)

# fruits = {"apple": "green", "banana": "yellow", "orange": "orange", "grapes": "purple"}
# print(fruits)
# print(fruits["banana"])
# fruits["banana"] = "light yellow"
# print(fruits)
# fruits["kiwi"] = "brown"
# print(fruits)
# print(len(fruits))
# # print(type(fruits))

# fruits["apple"] = "red"
# print(fruits)

# fruits.update({"apple": "dark red", "cherry": "pink"})
# print(fruits)

#pop() method removes the item with the specified key name:
# fruits = {"apple": "green", "banana": "yellow", "orange": "orange", "grapes": "purple"}

# safe_remove = fruits.pop("banana")
# print(safe_remove)
# print(fruits)

# #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

# inventory = {"apple": 5, "banana": 8, "orange": 12, "grapes": 15}

# inventory["apple"] -= 2
# inventory["banana"] += 5
# inventory.pop("orange")
# inventory["kiwi"] = 10
# print(inventory)

 
# student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student.keys())
# print(student.values())
# print(student.items())

#view objects
#The view objects contain the key-value pairs of the dictionary, as tuples in a list.

# my_dict = {"a": 1, "b": 2, "c": 3}
# keys_view = my_dict.keys()

# print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

# my_dict["d"] = 4
# print(keys_view)  # Output: dict_keys(['a', 'b', 'c', 'd'])
#The view object reflects the changes made to the dictionary.

#fromkeys() method
#The fromkeys() method returns a dictionary with the specified keys and value.  
#This method can be used to create a new dictionary from a list of keys.
# keys = ('a', 'b', 'c')
# default_value = 0

# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
# #If the value parameter is not specified, the default value will be None.
# new_dict2 = dict.fromkeys(keys)
# print(new_dict2)  # Output: {'a': None, 'b': None, 'c': None}
# #The fromkeys() method does not modify the original dictionary, it returns a new dictionary.
# #The fromkeys() method can be called on the dict class itself, or on an existing dictionary.
# existing_dict = {"x": 1, "y": 2}
# new_dict3 = existing_dict.fromkeys(keys, default_value)
# print(new_dict3)  # Output: {'a': 0, 'b': 0, 'c': 0}
# print(existing_dict)  # Output: {'x': 1, 'y': 2}
# # The existing_dict remains unchanged.

#Dictionary Comprehension
#Dictionary comprehension is a method for transforming one dictionary into another dictionary. 
#It is similar to list comprehension, but it creates a dictionary instead of a list.
original_dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value**2 for key, value in original_dict.items()}
print(squared_dict)  # Output: {'a': 1, 'b': 4, 'c': 9}
#In this example, we create a new dictionary called squared_dict by iterating over the items of original_dict and squaring each value.
#We use the items() method to get the key-value pairs of the original dictionary.
#The syntax for dictionary comprehension is similar to that of list comprehension, but we use curly braces {} instead of square brackets [].
#We also use a colon : to separate the key and value in the new dictionary.
#Dictionary comprehension can also include conditional statements to filter items from the original dictionary.
filtered_dict = {key: value for key, value in original_dict.items() if value % 2 != 0}
print(filtered_dict)  # Output: {'a': 1, 'c': 3}
#In this example, we create a new dictionary called filtered_dict by including only the items from original_dict where the value is odd.
#We use an if statement to filter the items based on the condition value % 2 != 0.
#Dictionary comprehension is a powerful and concise way to create new dictionaries from existing ones, and it can be used in various scenarios to transform and filter data.
#Note: Dictionary comprehension is available in Python 3.0 and later versions.

prices = {'apple': 0.40, 'banana': 0.50, 'orange': 0.60}
double_prices = {key: value * 2 for key, value in prices.items()}
print(double_prices)  # Output: {'apple': 0.8, 'banana': 1.0, 'orange': 1.2}

#In this example, we create a new dictionary called double_prices by iterating over the items of prices and multiplying each value by 2.
#We use the items() method to get the key-value pairs of the prices dictionary.

dict1 = {'x': 10, 'y': 20, 'z': 30}
dict2 = {key: value + 5 for key, value in dict1.items()}
dict1
print(dict1)  # Output: {'x': 10, 'y': 20, 'z': 30}

mega_dict = {**dict1, **dict2}
print(mega_dict)  # Output: {'x': 15, 'y': 25, 'z': 35}
#In this example, we create a new dictionary called dict2 by adding 5 to each value in dict1.

#Dictinoary vs tuples
#Dictionaries are used to store data values in key:value pairs, while tuples are used to store multiple items in a single variable.
#Dictionaries are mutable, meaning they can be changed after they are created, while tuples are immutable, meaning they cannot be changed after they are created.
#Dictionaries are unordered, meaning the items do not have a defined order, while tuples are ordered, meaning the items have a defined order.
#Dictionaries are defined using curly braces {}, while tuples are defined using parentheses ().
#Dictionaries are used when you need to associate values with keys, while tuples are used when you need to group related values together.
#Example of dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
#Example of tuple
coordinates = (10.0, 20.0)
print(coordinates)
#In summary, dictionaries are used for key-value pairs and are mutable and unordered, while tuples are used for grouping related values and are immutable and ordered.  
#The choice between using a dictionary or a tuple depends on the specific use case and the requirements of the data being stored.
#Dictionaries are generally more flexible and powerful than tuples, but tuples can be more efficient for certain use cases where immutability and order are important.

#json module
#The json module in Python is used to work with JSON (JavaScript Object Notation) data.
#JSON is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
import json

#Converting Python Object to JSON String
person_dict = {"name": "Alice", "age": 30, "city": "New York"}
person_json = json.dumps(person_dict)
print(person_json)  # Output: {"name": "Alice", "age": 30, "city": "New York"}
print(type(person_json))  # Output: <class 'str'>
#In this example, we use the json.dumps() method to convert a Python dictionary (person_dict) to a JSON string (person_json).

#Converting JSON String to Python Object
person_json = '{"name": "Alice", "age": 30, "city": "New York"}'
person_dict = json.loads(person_json)
print(person_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(person_dict))  # Output: <class 'dict'> 

#Dictionaires example mehtod for prod environment use
def get_user_info(user_id):
    # Simulate fetching user info from a database
    user_data = {
        1: {"name": "Alice", "age": 30, "city": "New York"},
        2: {"name": "Bob", "age": 25, "city": "Los Angeles"},
        3: {"name": "Charlie", "age": 35, "city": "Chicago"}
    }
    return user_data.get(user_id, {"error": "User not found"})
user_id = 2
user_info = get_user_info(user_id)
print(user_info)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

product_sales = {}
for sale in product_sales:
    product = sale["product"]
    quantity = sale["quantity"]
    if product in product_sales:
        product_sales[product] += quantity
    else:
        product_sales[product] = quantity
print(product_sales)  # Output: {'apple': 15, 'banana': 20, 'orange': 10}
