telephone_dir = {
    "tom": 9876543210,
    "rob": 8765432109,
    "joe": 7654321098
}

print("Tom's Number:", telephone_dir["tom"])

telephone_dir["sam"] = 6543210987
telephone_dir["tom"] = 1112223333

del telephone_dir["joe"]

for name, number in telephone_dir.items():
    print(f"Name: {name}, Phone: {number}")

point = (5, 9)
print("Tuple coordinates:", point)
print("X:", point[0], "Y:", point[1])
