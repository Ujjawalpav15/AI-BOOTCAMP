#WAP to calculate BMI (Body Mass Index). The formula to calculate BMI is weight(kg) / (height(m))^2
#Include error handling for zero or negative inputs

# def calculate_bmi(weight, height):
#     if weight <= 0 or height <= 0:
#         return "Error: Weight and height must be positive values."
#     bmi = weight / (height ** 2)
#     return bmi
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))   
# bmi=calculate_bmi(weight, height)
# print(f"Your BMI is: {bmi:.2f}")

#Create a function string_opeartions() that accepts a string as input and returns a tuple containing:
#the string in Uppercse, the string inowercase, the string with first letter capitalized, and the string reversed

# def string_operations(s):
#     upper_s = s.upper()
#     lower_s = s.lower()
#     capitalized_s = s.capitalize()
#     reversed_s = s[::-1]
#     return (upper_s, lower_s, capitalized_s, reversed_s)

# input_string = input("Enter a string: ")
# result = string_operations(input_string)
# print(result)


#Inplement a function process_numbers() that accpets a variable number of numeric arguments using *args,
#retunrs a dictionary with: 'sum': total of all numbers, 'average': average of numbers, 'max': maximum number, 'min': minimum number

# def process_numbers(*nums):
#     if len(nums) == 0:
#         return "Error: No numbers provided."
#     total = sum(nums)
#     average = total / len(nums)
#     maximum = max(nums)
#     minimum = min(nums)
#     return {'sum': total, 'average': average, 'max': maximum, 'min': minimum}

# result=process_numbers(10,20,30,40,50)
# print(result)

#Write a function validate_email() that takes an email address as parameter, returns
#True if email is valid (contains '@' and '.', '@' not first/last), returns False otherwise.
#Use only string methods , Use lamda function for validation

# def validate_email(email):
#     is_valid = lambda e: ('@' in e and '.' in e and e.index('@') > 0 and e.index('@') < len(e) - 1)
#     return is_valid(email)
# email_address = input("Enter an email address: ")
# if validate_email(email_address):
#     print(f"{email_address} is a valid email address.")
# else:
#     print(f"{email_address} is not a valid email address.")



#List Operations
# 1. Given a list numbers = [5, 2, 8, 1, 9], write code to sort it in ascending order.

# numbers = [5, 2, 8, 1, 9]
# numbers.sort()  
# print("Sorted List:", numbers)

#2. Create a new list containing only even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in original_list if num % 2 == 0]
# print("Even Numbers:", even_numbers)

#3. Write a program that takes two lists of equal length and returns a new list where
#each element is the sum of the corresponding elements from the input lists, then
#extend this to handle lists of unequal length by padding the shorter list with zeros.

# first_list = [1, 2, 3]
# second_list = [4, 5, 6,8]
# newlist=[first_list[i]+second_list[i] for i in range(len(first_list))]
# print("Summed List (Equal Length):", newlist)

# # Function to add two lists
# def add_lists(list1, list2):
#     result = []

#     # Find the length of the longer list
#     max_length = max(len(list1), len(list2))

#     # Loop through each index
#     for i in range(max_length):
#         # If index exists in list1, take the value, else take 0
#         if i < len(list1):
#             value1 = list1[i]
#         else:
#             value1 = 0

#         # If index exists in list2, take the value, else take 0
#         if i < len(list2):
#             value2 = list2[i]
#         else:
#             value2 = 0

#         # Add both values and store in result list
#         result.append(value1 + value2)

#     return result


# # Example lists
# list_a = [1, 2, 3, 4]
# list_b = [10, 20]

# # Function call
# sum_list = add_lists(list_a, list_b)

# # Output
# print("List A:", list_a)
# print("List B:", list_b)
# print("Sum List:", sum_list)


#Dictionary Operations

#1. Create a dictionary representing a book with keys for title, author and year.

# book={
#     "title": "To Kill a Mockingbird",
#     "author": "Harper Lee",
#     "year": 1960
# }

# print(book)

#2. Write code to add a new key-value pair "price":20 to an existing dictionary.

# book={
#     "title": "To Kill a Mockingbird",
#     "author": "Harper Lee",
#     "year": 1960
# }
# book["price"]=20
# print(book)'

#3. Create a dictionary that conuts how many times each letter apperas in the word "hello".

# word = "hello"
# letter_count = {}   
# for letter in word:
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1
# print(letter_count)

# 4. Write a function called invert_dictionary that takes a dictionary and returns a new
# dictionary where keys and values are swapped, handling collisions by storing the
# original keys as a list of values for any duplicate values in the input.

def invert_dictionary(original_dict):
    inverted_dict = {}

    for key, value in original_dict.items():
        # If the value is already a key in inverted_dict
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            # Create a new list with the key
            inverted_dict[value] = [key]

    return inverted_dict

data = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

result = invert_dictionary(data)
print(result)

# 5. Create a function named deep_merge that recursively merges two nested
# dictionaries, combining their contents such that if the same key exists in both, the
# values are merged recursively if they are dictionaries, otherwise the value from the
# second dictionary overwrites the first.

def deep_merge(dict1, dict2):
    merged = dict1.copy()  # Start with keys and values from dict1

    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            # If both values are dictionaries, merge them recursively
            merged[key] = deep_merge(merged[key], value)
        else:
            # Otherwise, overwrite with the value from dict2
            merged[key] = value

    return merged
dict_a = {
    'name': 'Alice',  
    'details': {
        'age': 30,
        'city': 'New York'
    }
}       
dict_b = {
    'details': {
        'age': 32,
        'country': 'USA'
    },
    'profession': 'Engineer'
}
merged_dict = deep_merge(dict_a, dict_b)
print(merged_dict)




        
