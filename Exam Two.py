def read_and_parse_csv(filename):
    Properties = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        start = 1 if lines[0].strip().lower().startswith("address") else 0

        for line in lines[start:]:
            parts = [part.strip() for part in line.strip().split(',')]

            if len(parts) != 5:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            address, city, state, zip_code, price_str = parts

            try:
                price = float(price_str)  
            except ValueError:
                print(f"Invalid price: {price_str} in line: {line.strip()}")
                continue

            row = [address, city, state, zip_code, price]
            Properties.append(row)

    return Properties


def calculate_zip_stats(Properties):
    Zip_Codes = []  

    for property in Properties:
        zip_code = property[3]
        price = property[4]

        found = False

        for row in Zip_Codes:
            if row[0] == zip_code:
                row[1] += 1
                row[2] += price
                found = True
                break

        if not found:
            Zip_Codes.append([zip_code, 1, price])

    for row in Zip_Codes:
        count = row[1]
        total = row[2]
        average = round(total / count, 2)
        row[2] = average

    return Zip_Codes

file_name = "Exam Two Properties.csv"
Properties = read_and_parse_csv(file_name)

print("Properties List:")
if not Properties:
    print("No properties found! Check your CSV file.")

else:
    for property in Properties:
        print(property)

Zip_Codes = calculate_zip_stats(Properties)

print("\n Zip Codes Summary:")

if not Zip_Codes:
    print("No zip code data found.") 

else:
    print("\n Zip Codes Summary:")

for row in Zip_Codes:
    zip_code, count, avg_price = row
    print(f"{zip_code:<10} {count:<8} {avg_price:>12.2f}")

