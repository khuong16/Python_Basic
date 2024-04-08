# if: đơn giản là kiểm tra điều kiện đầu vào
# sau đó trả về những thông tin cần thực hiện

# Tham số truyền vào if có thể là 1 giá trị.

friend = "Khuong"

user_name = input("Enter the name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")
else:
    print("Hello, stranger!")
    
print(bool(5))


# sử dụng từ khóa in trong if
friends = ["Khuong","An", "Anh"]
family = ["Hep pi"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friends!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")