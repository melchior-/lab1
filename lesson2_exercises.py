languages = ["Python", "JavaScript", "C++", "Java", "Ruby", "Go", "Swift", "Kotlin", "PHP", "TypeScript"]
first_language = languages[0]
last_language = languages[-1]
third_language = languages[2]
second_to_last_language = languages[-2]

print(languages[3:6])
print(languages[::2])
print(languages[::-1])

languages.append("Rust")
print(languages)
languages.insert(2, "C#")
print(languages)
languages.remove("Java")
print(languages)
languages.pop(4)
print(languages)

nums = [10, 20, 30, 40, 50]
length = len(nums)
min = min(nums)
max = max(nums)
sum = sum(nums)

nums1 = [432,532,234,52,1,2,3,4,5,6,7,8,9]
nums1 = nums1.sort()
nums1 = sorted(nums1, reverse=True)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a = list_b
# We need to use .copy to create a new list that is a copy of list_b, 
# so that changes to list_a do not affect list_b.
list_c = list_b.copy()

# Part B, Tuples and Unpacking

rgb = (255, 0, 0)
red = rgb[0]
green = rgb[1]
blue = rgb[2]
print(f"Red: {red}, Green: {green}, Blue: {blue}")

person = ("Martin", "Stockholm", 35)
name, city, age = person
print(f"Name: {name}, City: {city}, Age: {age}")


