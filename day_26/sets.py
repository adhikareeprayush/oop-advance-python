basket1 = {"apple", "orange", "apple", "banana"}
basket2 = {"orange", "kiwi", "banana"}

print("Unique Items Basket 1:", basket1)

print("Union:", basket1 | basket2)
print("Intersection:", basket1 & basket2)
print("Difference (Basket 1 - Basket 2):", basket1 - basket2)

fs = frozenset([1, 2, 3, 4])
print("Frozen Set:", fs)
