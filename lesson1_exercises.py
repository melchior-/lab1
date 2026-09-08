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

