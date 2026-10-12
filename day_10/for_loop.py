exp = [2340, 2500, 2100, 3100, 2980]
total = 0

for i in range(len(exp)):
    print(f"Month {i+1} Expense: {exp[i]}")
    total += exp[i]

print("Total Expense:", total)

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]

for location in locations:
    if location == key_location:
        print("Key found in:", location)
        break
    else:
        print("Key not in:", location)

print("Odd numbers between 1 and 10:")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
