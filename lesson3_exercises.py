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

