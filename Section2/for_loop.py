# for sẽ lặp theo số lần lặp biết trước.
# 1. giới thiệu cơ bản
friends = ["Khuong","Anh"]

for friend in friends:
    print(friend)
    
    
# 2. lặp phần tử theo số lượng
element = [0,1,2,3]

for _ in element:
    print("Hello, world!!!")
    
for index in range(2,20,3):
    print(index)
    
# 3. lặp thông qua list và dict:
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Annie", "grade": 70},
    {"name": "Peter", "grade": 60}   
]

for student in students:
    name = student["name"]
    print(name)