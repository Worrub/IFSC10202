# Functions are the code sections which are isolated from the rest of the program and executed only when called. 
# You've already met such functions as sqrt(), len() and print(). 
# They all have something in common: they take parameters (zero, one, or several of them), and they can return a value (or they can return nothing). 
# For example, the function sqrt() accepts one parameter and returns a value (the square root of the given number).
# The print() function can take various number of arguments and returns nothing.

#Now we want to show you how to write a function called factorial() which takes a single parameter — the number, and returns a value — the factorial of that number. 
# The def statement defines the name of the function and the name of values passed to it. 
# The return statement returns the value calculated by the function.

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
 
print(factorial(3))