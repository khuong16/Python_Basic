# dict:lưu trữ các key và value tương ứng.
# key : value
# dict sẽ ko chứa những giá trị key trùng lặp.

friend_age = {"Khuong": 24, "Son": 30, "Anh": 18}

friend_age["Bob"] = 45
friend_age["Khuong"] = 25

print(friend_age["Khuong"])
print(friend_age)


friends = (
    {"name": "Khuong", "age": 24},
    {"name": "Anh", "age": 18}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[0])

# change to dict: may be chỉ dùng với list.
friends_1 = [("Rolf", 24),("Anine", 25), ("Adame", 18)]
friends_change = dict(friends_1)
print(friends_change)