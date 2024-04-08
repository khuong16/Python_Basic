# set: các tập hợp ko đúng thứ tự về phần tử và sẽ
# không chưa giá trị trùng lặp

art_friends = {"Khuong","Anh"}
science_friends = {"Khuong","An"}

# làm nghệ thuật, nhưng ko làm khoa học.
art_but_not_science = art_friends.difference(science_friends)

# chọn ra những thằng ko chung cả 2 đối tượng
not_in_both = art_friends.symmetric_difference(science_friends)

# Chọn ra những thằng chung
art_and_science = art_friends.intersection(science_friends)

# union cả 2.
all_friends = art_friends.union(science_friends)

print(art_but_not_science)
print(not_in_both)
print(art_and_science)
print(all_friends)