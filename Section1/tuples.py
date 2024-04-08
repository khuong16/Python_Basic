# tuples: KHÔNG thể thêm được giá trị vào
# trong 1 tuples (ko dùng trick lỏ )

friends = "Khương", "Ánh"
friends_cleaner = ("Khương","Ánh")
# friends.append("Jen"): không append được do sẽ gây lỗi
# Nếu muốn thêm giá trị thì có thể: ( nhưng thường ko khuyến khích )
friends = friends + ("Jenny",)

print(friends)
print(friends_cleaner)