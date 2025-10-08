import re

input_filename = "07/07.Project Angles Input.txt"
output_filename = "07/07.Project Angles Output.txt"
converted_values = []

def dms_to_decimal_degrees(degrees, minutes, seconds):
    return float(degrees) + float(minutes) / 60 + float(seconds) / 3600 

def parse_dms_string(dms_string):
    match = re.match(r"(\d+)°(\d+)'(\d+)", dms_string)
    if match:
        return match.groups()
    else:
        return None

def process_coordinates(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        for line in infile:
            ddmmss_string = line.strip()
            if ddmmss_string:
                parts = parse_dms_string(ddmmss_string)
                if parts and len(parts) == 3:
                    degrees, minutes, seconds = parts
                    decimal_degrees = dms_to_decimal_degrees(degrees, minutes, seconds)
                    converted_values.append(f"{decimal_degrees:.6f}")
                else:
                    print(f"Invalid line format: {ddmmss_string}")

    with open(output_filename, 'w') as outfile:
        outfile.write('\n'.join(converted_values))

    print(f"Conversion complete. Decimal degrees written to '{output_filename}'.")

process_coordinates(input_filename, output_filename)
