import csv

def read_distance_csv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    cities = data[0][1:]

    distance_matrix = []
    for row in data[1:]:
        distances = list(map(int, row[1:])) 
        distance_matrix.append(distances)

    from_cities = [row[0] for row in data[1:]] 

    return from_cities, cities, distance_matrix

def print_distance_table(cities, distances):
    header = ["From/To"] + cities
    col_widths = [max(len(str(col)) for col in header)] + [10] * len(cities)
    
    header_row = " | ".join(str(item).ljust(width) for item, width in zip(header, col_widths))
    print(header_row)
    print("-+-".join("-" * width for width in col_widths))

    for from_city, row in zip(cities, distances):
        formatted_row = [from_city] + row
        print(" | ".join(str(item).ljust(width) for item, width in zip(formatted_row, col_widths)))

filename = "09/09.Project Distances.csv"

try:
    from_cities, to_cities, distances = read_distance_csv(filename)

    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")

    if from_city not in from_cities:
        print("Invalid From City")
    elif to_city not in to_cities:
        print("Invalid To City")
    else:
        from_index = from_cities.index(from_city)
        to_index = to_cities.index(to_city)
        distance = distances[from_index][to_index]

        print(f"\nDistance from {from_city} to {to_city}: {distance} miles\n")
        print("Full Distance Table:\n")
        print_distance_table(to_cities, distances)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
