def read_and_parse_csv(filename):
    Properties = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Skip header if it exists
        start = 1 if lines[0].strip().lower().startswith("address") else 0

        for line in lines[start:]:
            parts = line.strip().split(',')

            if len(parts) != 5:
                print(f"Skipping invalid line: {line.strip()}")
                continue

            address, city, state, zip_code, price_str = parts

            try:
                raw_price = float(price_str)
                adjusted_price = raw_price / 100.0  # move decimal left two places
            except ValueError:
                print(f"Invalid price: {price_str} in line: {line.strip()}")
                continue

            row = [address, city, state, zip_code, adjusted_price]
            Properties.append(row)

    return Properties


# Example usage
file_name = "Exam Two Properties.csv"
Properties = read_and_parse_csv(file_name)

# Print all properties
for property in Properties:
    print(property)