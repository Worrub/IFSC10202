## Create a python solution that reads a file containing angles in degrees, minutes, seconds format (DD°MM'SS"), converts the value to a decimal degree value, then write the values to a file.
# To simplify you code, you will need to create the following functions:
# ParseDegreeString(ddmmss) - inputs a location value and returns the degrees, minutes, and seconds
## Inputs
# ddmmss - inputs a string in the form of dd°mm'ss" and returns the degrees, minutes, and seconds
## Returns
# Degrees - Floating Point
# Minutes - Floating Point
# Seconds - Floating Point
## Logic
# Find the degree symbol (chr(176)) - degrees are between the beginning of the string and the position of the degree symbol.
# Find the minutes symbol (') - minutes are between the degree symbol and the minute symbol
# Find the seconds symbol(") - seconds are between the minutes symbol and the seconds symbol
# Return the degrees, minutes, and seconds as floating point
# DDMMSStoDecimal(degrees, minutes, seconds) - inputs degrees, minutes, and seconds and converts to a decimal value
## Inputs
# Degrees - Floating Point
# Minutes - Floating Point
# Seconds - Floating Point
## Returns
# Decimal Degrees - Floating Point
## Logic
# There are 60 minutes in a degree and 3600 seconds in a degree. 
# Calculate the decimals degrees as degrees plus minutes divided by 60 plus seconds divided by 3600.