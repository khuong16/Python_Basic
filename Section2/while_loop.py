# while: vòng lặp.
# có 2 dạng vòng lặp: for và while

is_learning = True

while is_learning:
    print("You're learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"
    
    
# c2
user_input = input("Do you want enter (yes/no): ")

while user_input == "yes":
    print("Program runninggg....")
    user_input = input("Do you want enter (yes/no): ")

print("Program stopped!!!")

# c3
user_input = input("Do you want enter (p/q): ")

while user_input != "q":
    if user_input == "p":
        print("Hello")
    user_input = input("Do you want enter (p/q): ")

print("Program stopped!!!")