# Lưu trữ nhiều giá trị trong 1 biến duy nhất
# List có 2 phương thức chính: append và remove

friend = ["Khuong",'Ánh',"Sơn"]
print(friend)
print(len(friend))

animal = [["Lion",25],["Monkey", 25]]
print(animal[0][1])

animal.append(["Dolphin",34])
print(animal)

animal.remove(["Monkey", 25])
print(animal)