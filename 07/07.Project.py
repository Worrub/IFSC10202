input_filename = "07/07.Project Angles Input.txt"
output_filename = "07/07.Project Angles Output.txt"
converted_values = []
ddmmss_to_decimal = []

def dms_to_decimal_degrees(degrees, minutes, seconds):
    return float(degrees) + float(minutes) / 60 + float(seconds) / 3600 

def process_coordinates(input_filename, output_filename):

    with open(input_filename, 'r') as infile:
        for line in infile:
            ddmmss_string = line.strip() 
        if ddmmss_string:
            decimal_degrees = ddmmss_to_decimal(ddmmss_string)
            if decimal_degrees is not None:
                converted_values.append(str(decimal_degrees))

    with open(output_filename, 'w') as outfile:
        outfile.write('\n'.join(converted_values))

    print(f"Conversion complete. Decimal degrees written to '{output_filename}'.")

