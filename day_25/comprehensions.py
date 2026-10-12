numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = [n**2 for n in numbers if n % 2 == 0]
print("Even Squares (List):", even_squares)

num_set = {1, 2, 3, 2, 3, 4, 5}
sq_set = {x**2 for x in num_set}
print("Squares (Set):", sq_set)

cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]
city_country_map = {city: country for city, country in zip(cities, countries)}
print("City-Country Mapping (Dict):", city_country_map)
