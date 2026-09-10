num = 3
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

