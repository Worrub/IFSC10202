start = int(input("Enter Start of Range: ", ))
end = int(input("Enter End of Range: ", ))

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
    return count

def is_special_number_number(num):
    if num < 0:
        return False
    if num == 0:
        return True
    
    order = count_digits(num)
    temp_num = num
    total_sum = 0
    
    while temp_num > 0:
        digit = temp_num % 10
        total_sum += digit ** order
        temp_num //= 10
        
    return total_sum == num

def find_special_number_in_range(start, end):
    print(f"Special Numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_special_number_number(number):
            print(number)

find_special_number_in_range (start, end)

#Create a program that displays special numbers in a range. 
#A special number is defined to be number that is the sum of its own digits each raised to the power of the number of digits.
#153 is 3 digits long and is equal to 1^3 + 5^3 + 3^3
#8208 is 4 digits long and is equal to 8^4 + 2^4 + 0^4 + 8^4
#First determine the number of digits using a while loop and reminder division by 10. Do not use any string functions or the len function.
#Recalculate the value using the power from above and see if you get the original value
#Do not use the len function to determine the number of digits.
#153 remainder divided gives 3 = number of digits, divided by 10 gives