# using f-string
age = 30
greeting = f"You are {age}"
print(greeting)

age = 24
print(greeting)

# using format c1
jose_name = "Jose"
final_greeting = "How are you, {} ?"
greeting_jose = final_greeting.format(jose_name)
print(greeting_jose)

# using format c2
jessic_name = "Jessic"
final_greeting = "How are you, {name} ?"
greeting_jessic = final_greeting.format(name=jessic_name)
print(greeting_jessic)