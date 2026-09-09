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

