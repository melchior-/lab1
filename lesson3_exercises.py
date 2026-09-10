num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

username = "martin"
password = "password123"
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if input_username == username and input_password == password:
    print("Login successful!")

score = 78
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

member = True
order_total = 120

if member and order_total > 100:
    discount = 0.1
    print(f"Discount applied: {discount * 100}%")

a = 5
b = 3

if a > b:
    print(f"{a} is greater than {b}")
if a < b:
    print(f"{a} is less than {b}")
if a == b:
    print(f"{a} is equal to {b}")
if a != b:
    print(f"{a} is not equal to {b}")
if a >= b:
    print(f"{a} is greater than or equal to {b}")
if a <= b:
    print(f"{a} is less than or equal to {b}")

# Part B

if "":
    print("This will not print because the string is empty.")
if "Hello":
    print("This will print because the string is not empty.")
if 0:
    print("This will not print because 0 is considered False.")
if 3:
    print("This will print because 3 is considered True")
if []:
    print("Will not print.")
if [1,2,3]:
    print("This will print.")

languages = ["Java", "C++", "Python"]
if "Java" in languages:
    print("Java is a language in the list.")

blocked_usernames = ["greg", "greta", "hans"]
if "greg" in blocked_usernames:
    print("greg is a blocked username")

roses_are_red = False
violets_are_blue = False

if not roses_are_red and not violets_are_blue:
    print("The garden will print.")

# Part C


