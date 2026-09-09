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

# We cannot change the values of a tuple, but we can create a 
# new tuple with the desired values.
# This is useful when we want to update the values of a 
# tuple without changing the original tuple.

list_of_tuples = [("Python", 3.9), ("Java", 15), ("C++", 11)]
for tuple in list_of_tuples:
    language, version = tuple
    print(f"Language: {language}, Version: {version}")

# Part C, Sets

list_of_courses = ["Python", "Java", "C++", "Python", "JavaScript", "Java"]
set_of_courses = set(list_of_courses)
print(len(list_of_courses))
print(len(set_of_courses))

skills1 = {"coding", "music", "maths", "machine learning", "building"}
skills2 = {"coding", "working", "music"}
shared_skills = skills1.intersection(skills2)

skills2.add("maths")
skills1.remove("building")
includes = "maths" in skills1

print(f"Shared skills: {shared_skills}")

