age = 25

result = age > 18 and age < 65 # true and true

print(result)

bool(0) # False, zero
bool(13) # True

bool("") # False, empty string
bool("Hello") # True

bool([]) # False, empty string
bool([1,3,5]) # True

# check
default_greeting = "There"
name = input("Enter your name (optional): ")

user_name = name or default_greeting
print(f"Hello, {user_name}")