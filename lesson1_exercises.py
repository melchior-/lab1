print("Martin Pettersson")
print("Lexicon Python and AI")
print("Today's study goal is to learn how to use Python for AI applications.")

name = "Martin Pettersson"
height = 1.89
student = True

print(type(name))
print(type(height))
print(type(student))

print(name)
print(height)
print(student)

print(type(height))
height = int(height)
print(type(height))

a = 53
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Three examples where explicit type conversion is necessary
# 1. Converting a string to an integer for mathematical operations
# 2. Converting a float to an integer to remove the decimal part
# 3. Converting an integer to a string for concatenation with other strings

# Part B

name = input("What is your name? ")
year_of_birth = input("What year were you born? ")
current_year = 2026
age = current_year - int(year_of_birth)
print(f"Hello, {name}! You are {age} years old.")

price_of_item = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
discount_amount = price_of_item * (discount_percentage / 100)
final_price = price_of_item - discount_amount
print(f"The discount amount is {discount_amount:.2f} and the final price is {final_price:.2f}.")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is {fahrenheit:.2f}.")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area:.2f} and the perimeter is {perimeter:.2f}.")

# If you type "hello" in length, it will cause a ValueError 
# because the input cannot be converted to a float.

# Part C

full_sentence = "      Roses are red, violets are blue."
print(len(full_sentence))
print(full_sentence.upper())
print(full_sentence.lower())
print(full_sentence.strip())

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name} {last_name}! Welcome to the program.")

first_name_lower = first_name.lower().strip()
last_name_lower = last_name.lower().strip()
username = first_name_lower[0:3] + "." + last_name_lower[0:5]
print(f"Your username is: {username}")

str = "python programming"
print(str[0])
print(str[-1])
print(str[0:6])
print(str[len(str)-11:])
print(str[::-1])

email = "martin.pettersson@outlook.com"
print(email.split("@")[0])
print(email.split("@")[1])

lang = "Java"
print(lang)
lang = "Python"
print(lang)

# Part D

str = "Python is a powerful programming language."
print(str[0:6])
print(str[7:9])
print(str[10:11])
print(str[12:21])
print(str[::-2])
print(str[::-1])
print(str[::-4])
print(str[::2])

ai = "Artificial Intelligence"
print(ai[0:10])
print(ai[11:22])
print(ai[::3])
print(ai[::-1])
print(ai[::-2])
print(ai[::-3])

# .split() method splits a string into a list of substrings 
# based on a specified delimiter.
# .strip() method removes leading and trailing whitespace from a string.
# .replace() method replaces occurrences of a specified 
# substring with another substring in a string.

# We demonstrate string immutability:
str = "Hello, World!"
# Attempting to change the first character of the string
# str[0] = "h"  # This will raise a TypeError because 
# strings are immutable in Python.
str = str.replace("H", "h") # This creates a new string with the desired change.

# Part E