items = ["bread", "pasta", "fruits", "veggies"]
print("Initial items:", items)

print("First item:", items[0])
print("Last item:", items[-1])
print("First 2 items:", items[0:2])

items[1] = "chips"
print("After modification:", items)

items.append("butter")
items.insert(1, "milk")
print("After append and insert:", items)

food = ["bread", "pasta"]
drinks = ["soda", "water"]
all_items = food + drinks
print("Combined List:", all_items)
print("Total Items:", len(all_items))
