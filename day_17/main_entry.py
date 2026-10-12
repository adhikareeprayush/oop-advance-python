# area of a circle for the given radius
def calculate_area(radius):
    return 3.14159 * (radius ** 2)


if __name__ == "__main__":
    print("Executing script directly...")
    r = 5
    area = calculate_area(r)
    print(f"Area of circle with radius {r}: {area}")
else:
    print("Script imported as a module!")
