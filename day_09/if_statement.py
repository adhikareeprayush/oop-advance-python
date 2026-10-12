num = 8

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "fried rice", "pot sticker"]
italian = ["pizza", "pasta", "risotto"]

dish = "samosa"

if dish in indian:
    print(f"{dish} is Indian cuisine")
elif dish in chinese:
    print(f"{dish} is Chinese cuisine")
elif dish in italian:
    print(f"{dish} is Italian cuisine")
else:
    print(f"Unknown cuisine for {dish}")
