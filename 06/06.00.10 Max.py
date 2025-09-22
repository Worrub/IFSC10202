# Here's the function max() that accepts two numbers and returns the maximum of them. 
# Actually, this function has already become the part of Python syntax.

def max(a, b):
    if a > b:
        return a
    else:
        return b
 
print(max(3, 5))
print(max(5, 3))
print(max(int(input("Enter First Number: ")), int(input("Enter Second Number: "))))