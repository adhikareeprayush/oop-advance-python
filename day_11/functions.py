# returns area of a rectangle or triangle, rectangle if shape not given
def calculate_area(dimension1, dimension2, shape="rectangle"):
    if shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        print("Unsupported shape")
        return None


rect_area = calculate_area(10, 20)
tri_area = calculate_area(10, 20, shape="triangle")

print("Rectangle Area:", rect_area)
print("Triangle Area:", tri_area)
